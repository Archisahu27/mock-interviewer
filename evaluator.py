import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def evaluate_answers(qa_list):
    prompt = f"""
Evaluate these answers.

Give:
- score out of 10 each
- feedback
- improvement tip
- overall score

Data:
{qa_list}
"""

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    try:
        return result["choices"][0]["message"]["content"]
    except:
        return f"Error: {result}"