import os

BASE_DIR = os.path.abspath("/data")

def _validate_path(file_path: str):
    abs_path = _validate_path(file_path)
    if os.path.commonpath([BASE_DIR, abs_path]) != BASE_DIR:
        raise PermissionError(f"Access to files outside {BASE_DIR} is not allowed")
    return abs_path

def read_text(file_path: str) -> str:
    abs_path = _validate_path(file_path)
    with open(abs_path, "r") as file:
        return file.read()

def read_json(file_path: str) -> dict[str, any] | list[dict[str, any]]:
    abs_path = _validate_path(file_path)
    with open(abs_path, "r") as file:
        return json.load(file)

def read_binary(file_path: str) -> bytes:
    abs_path = _validate_path(file_path)
    with open(abs_path, "rb") as file:
        return file.read()

def read_lines(file_path: str) -> list[str]:
    abs_path = _validate_path(file_path)
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
    return lines

def write_text(file_path: str, content: str):
    abs_path = _validate_path(file_path)
    with open(abs_path, "w") as file:
        file.write(content)

def write_json(file_path: str, content: dict[str, any] | list[dict[str, any]]): 
    abs_path = _validate_path(file_path)
    with open(abs_path, "w") as file:
        json.dump(content, file, indent=4)
