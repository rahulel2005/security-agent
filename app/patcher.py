import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def extract_json(text):
    if not text:
        raise ValueError("Empty response from model")

    text = text.strip()

    if text.startswith("```"):
        lines = text.splitlines()
        if len(lines) >= 3:
            text = "\n".join(lines[1:-1]).strip()

    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1 or end <= start:
        raise ValueError(f"No JSON object found in model response: {text}")

    return json.loads(text[start:end + 1])


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

    raw_content = response.choices[0].message.content
    print("Raw patch response:")
    print(raw_content)

    return extract_json(raw_content)