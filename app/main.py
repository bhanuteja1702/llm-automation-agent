import os
import json
from .tasks import *
from .openai_client import OpenAI
from fastapi import FastAPI, Response, HTTPException
from .file_utils import read_text
from pathlib import Path

app = FastAPI()

@app.post("/run")
async def run(response: Response, task: str = None):
    if not task:
        response.status_code = 400
        return;
    
    client = OpenAI()

    try:
        tools = client.get_tool_to_use(task)
        try:
            func_name = tools["choices"][0]["message"]["tool_calls"][0]["function"]["name"]
            func_args = tools["choices"][0]["message"]["tool_calls"][0]["function"]["arguments"]
            args = json.loads(func_args)

            globals()[func_name](**args)
        except Exception as e:
            response.status_code = 400
            return;

        response.status_code = 200
        return {"message": "Task completed successfully"}

    except HTTPException as http_err:
        response.status_code = http_err.status_code
        return;
    except Exception as err:
        response.status_code = 500
        return;       

@app.get("/read")
async def read(response: Response, file_path: str = None):
    if(file_path is None):
        response.status_code = 404
        return Response(content="", status_code=404)

    abs_path = os.path.abspath(file_path)
    path = Path(abs_path)
    if not path.exists() or not path.is_file():
        response.status_code = 404
        return Response(content="", status_code=404)
    
    try:
        content = read_text(file_path)
        return Response(content=content, media_type="text/plain")
    except Exception as e:
        response.status_code = 500
        return {"message": f"Error reading file: {str(e)}"}