import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_question(role, difficulty, previous_questions):
    prompt = f"""
You are a professional interviewer.

Ask ONE {difficulty} level interview question for a {role} role.

Do not repeat:
{previous_questions}

Only return the question.
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