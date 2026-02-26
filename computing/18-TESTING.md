# 18 — Modern Testing Stack

## The Big Picture

```
The Testing Landscape
======================

  What you're testing          Tool
  ═══════════════════          ════
  Pure logic / functions       Vitest (unit)
  React components             Testing Library + Vitest
  API endpoints                Supertest / Vitest + in-process server
  Browser flows end-to-end     Playwright
  Visual regression            Playwright screenshots / Chromatic
  API contracts                msw (mock service worker) / Pact
  Accessibility                axe-core (via Playwright or Testing Library)
  Performance                  Lighthouse CI / k6
```

```
The Testing Trophy (modern take on the pyramid)
================================================

          ┌─────────────┐
          │   E2E       │  few — slow, brittle, expensive
          │  Playwright │  but: only thing that catches full-stack issues
          ├─────────────┤
          │ Integration │  most — test modules working together
          │  + API      │  realistic, catches contract issues
          ├─────────────┤
          │    Unit     │  many — fast, isolated
          │   Vitest    │  but: don't test integration assumptions
          ├─────────────┤
          │   Static    │  always — TypeScript + ESLint
          │  Analysis   │  catches bugs before tests run
          └─────────────┘

  Classic pyramid inverted the ratio.
  Trophy: lean on integration tests more than pure unit tests.
  (Kent C. Dodds framing — widely adopted in JS ecosystem)
```

<!-- @editor[bridge/P2]: The trophy vs. pyramid distinction deserves a direct bridge for this reader. They built VSTS testing infrastructure around the classic pyramid (many unit tests, some integration, few E2E). The trophy's inversion — favoring integration over unit — was a reaction to the "mock trap" (heavy mocking producing tests that pass while integrations break). Worth one sentence: "If you built around the classic pyramid: the trophy doesn't discard it — it shifts weight from heavily-mocked unit tests toward integration tests that exercise real wiring, because JS/TS mocking was historically overused in ways that gave false confidence." -->

---

## Vitest — Unit & Integration Tests

Vitest is the modern replacement for Jest. Same API, runs natively in Vite's pipeline — no Babel transform, full TypeScript, ESM-native, dramatically faster.

```
Jest vs Vitest
===============

  Jest                           Vitest
  ════                           ══════
  Requires Babel transform       Native ESM, no transform needed
  CommonJS by default            ESM first
  Separate config from Vite      Shares vite.config.ts
  Slow cold start                Fast (Vite dev server reuse)
  jsdom built in                 jsdom optional (same API)
  Mature ecosystem               Jest-compatible — almost all Jest tests
                                 run unmodified
```

### Setup

```typescript
// vite.config.ts
import { defineConfig } from "vite";

export default defineConfig({
  test: {
    globals: true,          // describe/it/expect without imports
    environment: "node",    // or "jsdom" for browser APIs
    coverage: {
      provider: "v8",
      reporter: ["text", "lcov"],
      thresholds: { lines: 80 },
    },
  },
});
```

### Unit Tests

```typescript
// src/utils/format.ts
export function formatCurrency(amount: number, currency = "USD"): string {
  return new Intl.NumberFormat("en-US", { style: "currency", currency })
    .format(amount);
}

export function truncate(str: string, maxLength: number): string {
  if (str.length <= maxLength) return str;
  return str.slice(0, maxLength - 3) + "...";
}
```

```typescript
// src/utils/format.test.ts
import { describe, it, expect } from "vitest";
import { formatCurrency, truncate } from "./format";

describe("formatCurrency", () => {
  it("formats USD by default", () => {
    expect(formatCurrency(1234.5)).toBe("$1,234.50");
  });

  it("formats other currencies", () => {
    expect(formatCurrency(1000, "EUR")).toBe("€1,000.00");
  });
});

describe("truncate", () => {
  it("returns string unchanged if within limit", () => {
    expect(truncate("hello", 10)).toBe("hello");
  });

  it("truncates and adds ellipsis", () => {
    expect(truncate("hello world", 8)).toBe("hello...");
  });
});
```

### Mocking

```typescript
import { vi, describe, it, expect, beforeEach } from "vitest";
import { sendWelcomeEmail } from "./notifications";
import * as emailClient from "./emailClient";

// Mock an entire module
vi.mock("./emailClient");

describe("sendWelcomeEmail", () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it("sends email with correct subject", async () => {
    // Arrange
    const mockSend = vi.spyOn(emailClient, "sendEmail").mockResolvedValue({ id: "msg_123" });

    // Act
    await sendWelcomeEmail({ email: "user@example.com", name: "Alice" });

    // Assert
    expect(mockSend).toHaveBeenCalledWith(
      expect.objectContaining({
        to: "user@example.com",
        subject: expect.stringContaining("Welcome"),
      })
    );
  });

  it("throws if email client fails", async () => {
    vi.spyOn(emailClient, "sendEmail").mockRejectedValue(new Error("SMTP error"));
    await expect(sendWelcomeEmail({ email: "bad@example.com", name: "Bob" }))
      .rejects.toThrow("SMTP error");
  });
});
```

### Integration Test — API Route

```typescript
// Test the full Express route handler with a real (in-memory) DB
import { describe, it, expect, beforeAll, afterAll } from "vitest";
import request from "supertest";
import { app } from "../app";
import { db } from "../db";

beforeAll(async () => {
  await db.migrate.latest();   // run migrations on test DB
});

afterAll(async () => {
  await db.destroy();
});

describe("POST /api/orders", () => {
  it("creates order and returns 201", async () => {
    const res = await request(app)
      .post("/api/orders")
      .set("Authorization", "Bearer test-token")
      .send({ productId: "prod_123", quantity: 2 });

    expect(res.status).toBe(201);
    expect(res.body).toMatchObject({
      id: expect.any(String),
      status: "pending",
      quantity: 2,
    });
  });

  it("rejects missing productId with 400", async () => {
    const res = await request(app)
      .post("/api/orders")
      .set("Authorization", "Bearer test-token")
      .send({ quantity: 2 });

    expect(res.status).toBe(400);
    expect(res.body.error).toMatch(/productId/);
  });
});
```

### Snapshot Testing

```typescript
it("renders correct HTML structure", () => {
  const html = renderEmailTemplate({ name: "Alice", orderId: "ord_456" });
  expect(html).toMatchSnapshot();   // first run: creates snapshot file
                                     // subsequent runs: diffs against it
});
// Update snapshots: vitest --update-snapshots
```

Use snapshots sparingly. Good for: serialized output (HTML, JSON config), generated code. Bad for: anything that changes frequently or has meaningful logic to assert.

---

## Testing Library — Component Tests

Testing Library's philosophy: test components the way users interact with them, not their implementation. Query by what's visible, not by CSS class or component internals.

```
Implementation testing (bad)       Behavior testing (good)
════════════════════════════       ══════════════════════════

  wrapper.find('.submit-btn')        screen.getByRole('button', { name: /submit/i })
  component.state.isLoading          screen.getByText('Loading...')
  component.props.onClick            userEvent.click(button)

  Breaks on refactor                 Survives refactor
  Doesn't test user experience       Tests actual user experience
```

### React Component Test

```typescript
// src/components/LoginForm.test.tsx
import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { vi } from "vitest";
import { LoginForm } from "./LoginForm";

describe("LoginForm", () => {
  it("calls onSubmit with email and password", async () => {
    const onSubmit = vi.fn().mockResolvedValue(undefined);
    render(<LoginForm onSubmit={onSubmit} />);

    await userEvent.type(screen.getByLabelText(/email/i), "user@example.com");
    await userEvent.type(screen.getByLabelText(/password/i), "password123");
    await userEvent.click(screen.getByRole("button", { name: /sign in/i }));

    await waitFor(() => {
      expect(onSubmit).toHaveBeenCalledWith({
        email: "user@example.com",
        password: "password123",
      });
    });
  });

  it("shows validation error for empty email", async () => {
    render(<LoginForm onSubmit={vi.fn()} />);
    await userEvent.click(screen.getByRole("button", { name: /sign in/i }));
    expect(screen.getByText(/email is required/i)).toBeInTheDocument();
  });

  it("disables button while submitting", async () => {
    const onSubmit = vi.fn(() => new Promise(r => setTimeout(r, 100)));
    render(<LoginForm onSubmit={onSubmit} />);

    await userEvent.type(screen.getByLabelText(/email/i), "user@example.com");
    await userEvent.type(screen.getByLabelText(/password/i), "pass");
    await userEvent.click(screen.getByRole("button", { name: /sign in/i }));

    expect(screen.getByRole("button", { name: /signing in/i })).toBeDisabled();
  });
});
```

### Query Priority (use in this order)

```
1. getByRole          → 'button', 'textbox', 'heading', 'link'  (best)
2. getByLabelText     → form fields with labels
3. getByPlaceholderText → fallback for unlabeled inputs
4. getByText          → text content visible on screen
5. getByDisplayValue  → current value of input/select
6. getByAltText       → img alt text
7. getByTitle         → title attribute
8. getByTestId        → data-testid attribute  (last resort)
```

---

## MSW — Mock Service Worker

MSW intercepts network requests at the service worker or Node.js level. Your component makes real `fetch()` calls; MSW intercepts them. No axios mocking, no manual stubs per test.

```
Without MSW                        With MSW
═══════════════                    ════════

  vi.mock("./api/orders")            Component calls fetch() normally
  vi.mock("axios")                   MSW intercepts at network level
  mockFetch.mockResolvedValue(...)   One set of handlers for all tests
                                     AND the browser during development
  Brittle, tied to implementation    Tests that actually hit the network path
```

### Setup

```typescript
// src/mocks/handlers.ts
import { http, HttpResponse } from "msw";

export const handlers = [
  http.get("/api/orders", () => {
    return HttpResponse.json([
      { id: "ord_1", status: "pending", total: 99.99 },
      { id: "ord_2", status: "shipped", total: 49.99 },
    ]);
  }),

  http.post("/api/orders", async ({ request }) => {
    const body = await request.json();
    return HttpResponse.json(
      { id: "ord_new", status: "pending", ...body },
      { status: 201 }
    );
  }),

  http.get("/api/orders/:id", ({ params }) => {
    if (params.id === "ord_999") {
      return new HttpResponse(null, { status: 404 });
    }
    return HttpResponse.json({ id: params.id, status: "pending" });
  }),
];
```

```typescript
// src/mocks/server.ts  (Node.js — for Vitest)
import { setupServer } from "msw/node";
import { handlers } from "./handlers";

export const server = setupServer(...handlers);

// src/test/setup.ts
import { server } from "../mocks/server";
beforeAll(() => server.listen({ onUnhandledRequest: "error" }));
afterEach(() => server.resetHandlers());   // prevent handler leak between tests
afterAll(() => server.close());
```

```typescript
// Override per-test
import { server } from "../mocks/server";
import { http, HttpResponse } from "msw";

it("shows error state when API fails", async () => {
  server.use(
    http.get("/api/orders", () => new HttpResponse(null, { status: 500 }))
  );

  render(<OrderList />);
  expect(await screen.findByText(/failed to load/i)).toBeInTheDocument();
});
```

---

## Playwright — End-to-End Tests

Playwright drives real browsers (Chromium, Firefox, WebKit). The gold standard for E2E in the Node ecosystem — replaced Cypress as the default recommendation.

```
Playwright vs Cypress
======================

  Cypress                        Playwright
  ═══════                        ══════════
  Chromium only (+ experimental) Chromium, Firefox, WebKit
  Runs inside browser            Runs outside browser (Node process)
  Time-travel debugging          Trace viewer (same idea, better)
  Single tab/origin              Multi-tab, multi-origin, iframes
  Slower parallelism             Fast parallel by default
  Great DX for simple apps       Better for complex flows + multi-browser
  Huge ecosystem                 Growing fast, Microsoft-backed
```

### Setup

```bash
npm init playwright@latest
# creates playwright.config.ts, example tests, installs browsers
```

```typescript
// playwright.config.ts
import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "./e2e",
  fullyParallel: true,
  retries: process.env.CI ? 2 : 0,    // retry flaky tests in CI
  reporter: "html",
  use: {
    baseURL: "http://localhost:3000",
    trace: "on-first-retry",           // capture trace on failure
    screenshot: "only-on-failure",
  },
  projects: [
    { name: "chromium", use: { ...devices["Desktop Chrome"] } },
    { name: "firefox", use: { ...devices["Desktop Firefox"] } },
    { name: "mobile", use: { ...devices["iPhone 13"] } },
  ],
  webServer: {
    command: "npm run dev",
    url: "http://localhost:3000",
    reuseExistingServer: !process.env.CI,
  },
});
```

### Writing Tests

```typescript
// e2e/checkout.spec.ts
import { test, expect } from "@playwright/test";

test.describe("Checkout flow", () => {
  test.beforeEach(async ({ page }) => {
    // Log in via API (faster than UI login every test)
    await page.request.post("/api/test/login", {
      data: { email: "test@example.com", password: "password" },
    });
    await page.goto("/cart");
  });

  test("completes purchase with valid card", async ({ page }) => {
    await page.getByRole("button", { name: /checkout/i }).click();

    await page.getByLabel(/card number/i).fill("4242 4242 4242 4242");
    await page.getByLabel(/expiry/i).fill("12/26");
    await page.getByLabel(/cvc/i).fill("123");
    await page.getByRole("button", { name: /pay now/i }).click();

    // Wait for navigation to confirmation page
    await expect(page).toHaveURL(/\/order\/ord_/);
    await expect(page.getByRole("heading", { name: /order confirmed/i }))
      .toBeVisible();
  });

  test("shows error for declined card", async ({ page }) => {
    await page.getByRole("button", { name: /checkout/i }).click();
    await page.getByLabel(/card number/i).fill("4000 0000 0000 0002"); // Stripe test decline
    await page.getByRole("button", { name: /pay now/i }).click();

    await expect(page.getByText(/card was declined/i)).toBeVisible();
  });
});
```

### Page Object Model

```typescript
// e2e/pages/CheckoutPage.ts
import { Page, Locator } from "@playwright/test";

export class CheckoutPage {
  readonly cardNumber: Locator;
  readonly expiry: Locator;
  readonly cvc: Locator;
  readonly payButton: Locator;

  constructor(private page: Page) {
    this.cardNumber = page.getByLabel(/card number/i);
    this.expiry = page.getByLabel(/expiry/i);
    this.cvc = page.getByLabel(/cvc/i);
    this.payButton = page.getByRole("button", { name: /pay now/i });
  }

  async fillCard(number: string, expiry: string, cvc: string) {
    await this.cardNumber.fill(number);
    await this.expiry.fill(expiry);
    await this.cvc.fill(cvc);
  }

  async submit() {
    await this.payButton.click();
  }
}
```

### Playwright Tooling

```bash
npx playwright test                     # run all E2E tests
npx playwright test --headed            # show browser
npx playwright test --debug             # step through with inspector
npx playwright show-report              # open HTML report
npx playwright codegen http://localhost:3000  # record clicks → generate code
```

---

## Contract Testing — Pact

<!-- @editor[content/P1]: Contract testing (Pact) appears in the landscape diagram but has no section in the file. The calibration notes specifically call this out: "no direct .NET contract testing equivalent (Pact is new)." This is the one testing concept in the landscape where there's no prior art to bridge from — it deserves a section with the consumer-driven contracts concept, a minimal Pact example, and a note that the .NET world had no equivalent (the closest was WCF WSDL contracts, which were provider-driven not consumer-driven). Without this section, the landscape diagram promises content that doesn't exist. -->

---

## Coverage

```bash
# Vitest coverage
vitest run --coverage

# Output:
# ────────────────────────────────────────────────
# File             | % Lines | % Branch | % Funcs
# ────────────────────────────────────────────────
# utils/format.ts  |   100   |   100    |   100
# api/orders.ts    |    87   |    75    |    90
# ────────────────────────────────────────────────
```

Coverage measures what code your tests execute, not whether they assert correctly. 100% coverage can coexist with terrible tests. Use it as a floor (catch forgotten paths), not a ceiling (not a quality metric).

---

## CI Integration

```yaml
# .github/workflows/ci.yml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20, cache: npm }
      - run: npm ci

      # Unit + integration
      - run: vitest run --coverage
      - uses: actions/upload-artifact@v4
        with: { name: coverage, path: coverage/ }

  e2e:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20, cache: npm }
      - run: npm ci
      - run: npx playwright install --with-deps chromium
      - run: npx playwright test
      - uses: actions/upload-artifact@v4
        if: failure()                           # only upload on failure
        with:
          name: playwright-report
          path: playwright-report/
```

---

## Common Confusion Points

**`getByRole` queries are the most important thing to learn.**
They test accessibility and behavior simultaneously. If you can't find an element by role, it often means the component has an accessibility problem. `button`, `link`, `heading`, `textbox`, `checkbox`, `combobox`, `dialog`, `alert` — learn these.

**Don't test implementation details.**
Testing that `useState` was called, or that a specific CSS class was applied, makes tests brittle. Tests should break when behavior changes, not when you refactor internals.

**`await userEvent` not `fireEvent`.**
`fireEvent.click()` fires a single DOM event. `userEvent.click()` simulates the full user interaction sequence (focus, pointer events, click, blur). Use `userEvent` for realistic tests. Note: `userEvent` methods are async in v14+.

**MSW `onUnhandledRequest: "error"` is your friend.**
In test setup, set this. If your component makes a fetch call you didn't mock, the test fails loudly instead of silently returning undefined. Catches missing mocks immediately.

**E2E tests should use test IDs on the server, not mock everything.**
The value of E2E is exercising the real stack. Use a test database, seed it with known data, run real API calls. If you mock the API in Playwright tests, you're only testing the frontend — which you already covered with component tests.

**Playwright `waitFor` vs `findBy` vs auto-waiting.**
Playwright has built-in auto-waiting — locators automatically wait for elements to be visible and stable. You rarely need explicit `waitFor`. Testing Library's `findBy*` queries are the async equivalent of `getBy*`.

---

## Old World Bridge

| .NET / MSTest / Classic Testing | Modern JS Testing |
|---|---|
| MSTest / NUnit / xUnit | Vitest (same concepts: describe, test, assert) |
| `[TestMethod]` / `[Fact]` | `it("...", () => {})` |
| `Assert.AreEqual(expected, actual)` | `expect(actual).toBe(expected)` |
| `[TestInitialize]` / constructor | `beforeEach(() => {})` |
| `[TestCleanup]` | `afterEach(() => {})` |
| Moq / NSubstitute | `vi.mock()` / `vi.spyOn()` |
| Integration tests with TestServer | Supertest with Express app |
| Selenium / WebDriver | Playwright |
| Coded UI Tests | Playwright (same concept, much better DX) |
| Code coverage (dotCover / OpenCover) | Vitest coverage (v8 / istanbul) |
| Test Explorer in Visual Studio | Vitest UI (`vitest --ui`) |

---

## Decision Cheat Sheet

| I want to test... | Use |
|---|---|
| Pure function / business logic | Vitest unit test |
| React component behavior | Testing Library + Vitest |
| API route with real DB | Supertest + Vitest integration test |
| Component that fetches data | Testing Library + MSW |
| Full browser flow (user journey) | Playwright E2E |
| Multiple browsers | Playwright (Chromium, Firefox, WebKit) |
| Visual regression | Playwright screenshots or Chromatic |
| Accessibility | axe-core via `@axe-core/playwright` or Testing Library |
| API mocking without changing component code | MSW |
| Snapshot of rendered output | Vitest `toMatchSnapshot()` |
| Code coverage | Vitest `--coverage` with v8 provider |
| Generate test code from clicking | `playwright codegen` |
| Run only tests matching a pattern | `vitest run utils` or `playwright test checkout` |
