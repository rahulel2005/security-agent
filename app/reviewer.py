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


def review_patch(finding, original_code, patch):
    prompt = open("prompts/review.txt", "r", encoding="utf-8").read()

    user_payload = {
        "finding": finding,
        "original_code": original_code,
        "patch": patch
    }

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": json.dumps(user_payload)}
        ]
    )

    raw_content = response.choices[0].message.content
    print("Raw review response:")
    print(raw_content)

    return extract_json(raw_content)