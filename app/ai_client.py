import os
from anthropic import Anthropic

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def ask_ai(prompt: str):
    msg = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )
    return msg.content[0].text
