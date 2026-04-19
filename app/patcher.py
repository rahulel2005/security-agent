import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_patch(finding, file_content):
    prompt = open("prompts/patch.txt", "r", encoding="utf-8").read()

    user_payload = {
        "finding": finding,
        "file_content": file_content
    }

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": json.dumps(user_payload)}
        ]
    )

    return json.loads(response.choices[0].message.content)