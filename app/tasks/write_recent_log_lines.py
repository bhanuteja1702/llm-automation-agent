from pathlib import Path

def write_recent_log_lines(log_dir: str, output_file: str, count: int = 10):
    log_path = Path(log_dir)
    log_files = list(log_path.glob("*.log"))
    log_files_sorted = sorted(log_files, key=lambda f: f.stat().st_mtime, reverse=True)
    recent_files = log_files_sorted[:count]

    first_lines = []
    for log_file in recent_files:
        try:
            with log_file.open("r") as f:
                first_line = f.readline().strip()
                first_lines.append(first_line)
        except Exception as e:
            print(f"Error reading {log_file}: {e}")
            first_lines.append("")
    
    with open(output_file, "w") as outfile:
        for line in first_lines:
            outfile.write(line + "\n")