import os
import json
import httpx
from pathlib import Path

AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")

class OpenAI:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(OpenAI, cls).__new__(cls)
            cls._instance._init_instance()
        return cls._instance

    def _init_instance(self):
        self.token = os.getenv("AIPROXY_TOKEN")

    def _get_tools(self) -> dict[str, any]:
        tools_json_path = os.path.join(os.path.dirname(__file__), "tools.json")
        print(tools_json_path)
        with open(tools_json_path, "r") as file:
            return json.load(file)["tools"]

    def completion(self, user_input: list[dict[str, any]]) -> dict[str, any]:
        response = httpx.post(
            "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4o-mini",
                "messages": user_input,
            },
            timeout=17
        )
        return response.json()

    def get_tool_to_use(self, user_input: str) -> dict[str, any]:
        response = httpx.post(
            "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [{"role": "user", "content": user_input}],
                "tools": self._get_tools()
            },
            timeout=17
        )
        print(response.json())
        return response.json()
    
    def get_embeddings(self, text: str) -> dict[str, any]:
        response = httpx.post(
            "https://aiproxy.sanand.workers.dev/openai/v1/embeddings",
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            },
            json={"model": "text-embedding-3-small", "input": text},
            timeout=17
        )
        print(response.json())
        return response.json()



