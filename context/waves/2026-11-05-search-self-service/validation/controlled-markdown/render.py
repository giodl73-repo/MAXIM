from pathlib import Path
import markdown,sys,importlib.util,json
spec=importlib.util.spec_from_file_location('builder',sys.argv[2]);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
raw=Path(sys.argv[1]).read_text(encoding='utf-8');html=markdown.markdown(raw);print(json.dumps(dict(version=markdown.__version__,html=html,text=m.plain(html)),ensure_ascii=False))
