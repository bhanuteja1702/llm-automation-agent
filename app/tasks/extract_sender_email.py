import json
from os import path
from ..openai_client import OpenAI
from ..file_utils import read_text, write_text

def extract_sender_email(input_file: str, output_file: str):
    client = OpenAI()
   
    email = read_text(input_file)
    prompt = [{"role": "user","content": f"Extract the sender's email address from the following email message. Return only the email address with no additional text or formatting.<email>{email}</email>".strip()}]
    completion = client.completion(prompt)
    sender_email = completion["choices"][0]["message"]["content"]

    write_text(output_file, sender_email)
