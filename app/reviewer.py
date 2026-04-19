import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def review_patch(finding, patch):
    prompt = open("prompts/review.txt").read()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"{finding}\n{patch}"}
        ]
    )

 import json
return json.loads(response.choices[0].message.content)