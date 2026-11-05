// Execute actual unknown-target WASM and original native Index over identical bytes.
// Artifacts remain outside the source tree. No tolerant/rounded score comparisons.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {spawnSync} from 'node:child_process';
import {createHash} from 'node:crypto';
import {gzipSync} from 'node:zlib';

const [input,pkg,control,output]=process.argv.slice(2);
if(!output)throw new Error('Usage: node tools/check-search.mjs INDEX_JSON PKG_DIR NATIVE_CONTROL NEW_OUTPUT_DIR');
fs.mkdirSync(output);const raw=fs.readFileSync(input);const sha=data=>createHash('sha256').update(data).digest('hex');
const queries=[];
for(const query of ['rust ownership','entropy','ocean currents','game theory','climate','decision','réseau','植物'])
 for(const section of ['','languages','not-a-real-module'])
  for(const limit of [0,1,20,100,1000])queries.push({query,section,limit});
for(const query of ['', ' \t\n', '!?', 'zzzznomatchingentryzzzz', 'Rust RUST ownership', 'RUST OWNERSHIP', 'rust-ownership', 'é'.repeat(256),'é'.repeat(257),'r'.repeat(512),'r'.repeat(513),Array.from({length:16},(_,i)=>`term${i}`).join(' '),Array.from({length:17},(_,i)=>`term${i}`).join(' ')])
 queries.push({query,section:'',limit:20});
queries.push({query:'entropy',section:'',limit:4294967295});
fs.writeFileSync(path.join(output,'controls.json'),JSON.stringify(queries,null,2)+'\n');
const native=spawnSync(control,[input],{input:queries.map(q=>JSON.stringify(q)).join('\n')+'\n',encoding:'utf8',maxBuffer:256*1024*1024,timeout:180000});
fs.writeFileSync(path.join(output,'native.stdout.gz'),gzipSync(native.stdout??''));fs.writeFileSync(path.join(output,'native.stderr'),native.stderr??'');
if(native.status!==0)throw new Error(`Native control failed: ${native.status} ${native.error??native.stderr}`);
const lines=native.stdout.trimEnd().split('\n').map(s=>JSON.parse(s));if(lines.length!==queries.length+1)throw new Error('Native record count mismatch');
const wasmPath=path.resolve(pkg,'maxim_search_bg.wasm');const bytes=fs.readFileSync(wasmPath);const module=await WebAssembly.compile(bytes);
const adapter=await import(pathToFileURL(path.resolve(pkg,'maxim_search.js')));await adapter.default({module_or_path:bytes});
const index=new adapter.SearchIndex(raw.toString('utf8'));
if(lines[0].count!==index.count()||lines[0].sections_json!==index.sections())throw new Error('Native/WASM count or sections mismatch');
const actual=[],mismatches=[];
for(const [i,q]of queries.entries()){
 const json=index.search(q.query,q.section,q.limit);actual.push({ok:true,json});
 if(json!==lines[i+1].json)mismatches.push({control:i,inputs:q,native_sha256:sha(lines[i+1].json),wasm_sha256:sha(json)});
}
fs.writeFileSync(path.join(output,'wasm.stdout.gz'),gzipSync(actual.map(x=>JSON.stringify(x)).join('\n')+'\n'));
const constructors=[];const entry={title:'Fixture',url:'fixture/',section:'fixture',text:'fixture'};
for(const [name,value]of [['empty',JSON.stringify({version:1,entries:[],terms:{}})],['syntax','{'],['missing-fields','{}'],['unsupported-version',JSON.stringify({version:2,entries:[],terms:{}})],['out-of-range-posting',JSON.stringify({version:1,entries:[entry],terms:{fixture:[[1,1]]}})],['duplicate-posting',JSON.stringify({version:1,entries:[entry],terms:{fixture:[[0,1],[0,2]]}})],['negative-weight',JSON.stringify({version:1,entries:[entry],terms:{fixture:[[0,-1]]}})]]){
 const filename=path.join(output,`constructor-${name}.json`);fs.writeFileSync(filename,value);
 const observed=spawnSync(control,[filename],{encoding:'utf8',input:'',timeout:15000});const expected=JSON.parse(observed.stdout.trim());let result;
 try{const checked=new adapter.SearchIndex(value);result={ok:true,count:checked.count(),sections_json:checked.sections()};checked.free();}catch(error){result={ok:false,error:String(error)};}
 if(expected.ok?observed.status!==0:observed.status!==2)throw new Error('Unexpected native constructor process exit');
 const exact=expected.ok?result.ok&&expected.count===result.count&&expected.sections_json===result.sections_json:!result.ok&&expected.error===result.error;
 constructors.push({name,native_exit:observed.status,native:expected,wasm:result,exact});
}
fs.writeFileSync(path.join(output,'constructor-controls.json'),JSON.stringify(constructors,null,2)+'\n');
// JavaScript coerces raw numbers to wasm32 usize before Rust receives them.
// These observations are intentionally outside the typed parity assertion.
const abi=[4294967296,4294967297,1.5,-1].map(limit=>({limit,coerced_u32:limit>>>0,result:index.search('entropy','',limit)}));
fs.writeFileSync(path.join(output,'raw-js-abi.json.gz'),gzipSync(JSON.stringify(abi)));
const record={schema:'maxim.search-parity.v1',input:{path:path.resolve(input),bytes:raw.length,sha256:sha(raw)},wasm:{bytes:bytes.length,sha256:sha(bytes),imports:WebAssembly.Module.imports(module)},native:{path:path.resolve(control),sha256:sha(fs.readFileSync(control))},entries:index.count(),sections:JSON.parse(index.sections()).length,controls:queries.length,constructor_controls:constructors.length,all_exact:mismatches.length===0&&constructors.every(x=>x.exact),mismatches,raw_js_abi_controls_separate:abi.length,scope:'Exact same-index native/WASM Results serialization, totals, scores, ordering, complete entry text, sections and count, plus small explicit constructor/empty/corruption controls. Actual published index input is an observation; original MkDocs/source-to-index lineage and complete release custody remain separate. Native binary/toolchain and shared compiled target are installed prerequisites; no clean-cache claim.'};
fs.writeFileSync(path.join(output,'receipt.json'),JSON.stringify(record,null,2)+'\n');index.free();console.log(JSON.stringify(record));if(!record.all_exact)process.exitCode=1;
