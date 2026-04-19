import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


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

    return json.loads(response.choices[0].message.content)