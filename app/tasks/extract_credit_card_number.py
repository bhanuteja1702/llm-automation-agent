import json
import httpx
from os import path
import base64
import mimetypes
from ..openai_client import OpenAI
from ..file_utils import read_binary, write_text


def extract_credit_card_number(image_path: str, output_file: str):
    client = OpenAI()

    mime_type, _ = mimetypes.guess_type(image_path)
    if mime_type is None:
        raise ValueError("Could not determine the image type.")

    base64_image = base64.b64encode(read_binary(image_path)).decode("utf-8")
    prompt = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Extract the credit card number from the image. Return only the number without spaces.",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:{mime_type};base64,{base64_image}"},
                }
            ]
        }
    ]
    completion = client.completion(prompt)
    print(completion)
    card_number = completion["choices"][0]["message"]["content"].strip().replace(
        " ", "")

    write_text(output_file, card_number)
