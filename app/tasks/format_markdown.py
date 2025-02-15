from os import path
import subprocess

def format_markdown(input_file: str, prettier_version: str):
    abs_path = path.abspath(input_file)
    subprocess.run(f"npx prettier@{prettier_version} {abs_path} --write --parser markdown", shell=True, check=True)