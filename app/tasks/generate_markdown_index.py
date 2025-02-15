from pathlib import Path
import json

def generate_markdown_index(docs_dir: str, index_file: str):
    base_path = Path(docs_dir)
    index = {}

    for md_file in base_path.glob("**/*.md"):
        relative_path = md_file.relative_to(base_path).as_posix()
        
        title = ""
        try:
            with md_file.open("r", encoding="utf-8") as f:
                for line in f:
                    stripped = line.strip()
                    if stripped.startswith("# "):
                        title = stripped[1:].strip()
                        break
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
        
        index[relative_path] = title

    with open(index_file, "w", encoding="utf-8") as out:
        json.dump(index, out, indent=2)