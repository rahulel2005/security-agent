import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def run_triage(finding):
    prompt = open("prompts/triage.txt", "r", encoding="utf-8").read()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": json.dumps(finding)}
        ]
    )

    return json.loads(response.choices[0].message.content)