import os
 import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_patch(finding):
    prompt = open("prompts/patch.txt").read()

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": str(finding)}
        ]
    )

   
return json.loads(response.choices[0].message.content)