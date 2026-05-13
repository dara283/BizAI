from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_ai_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a Business Operations Analyst AI. Analyse business data, identify problems, summarise reports, and give improvement suggestions. Keep answers clear, structured, and professional."
            },
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content