import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def review_patch(finding, patch):
    prompt = open("prompts/review.txt", "r", encoding="utf-8").read()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": json.dumps({
                    "finding": finding,
                    "patch": patch
                })
            }
        ]
    )

    return json.loads(response.choices[0].message.content)