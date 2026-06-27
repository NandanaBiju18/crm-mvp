import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_followup(lead):
    prompt = f"""
You are a professional sales executive of ISM Training Institute.

Lead Details:
Name: {lead.name}
Interest: {lead.interest}
Status: {lead.status}
Category: {lead.category}
Score: {lead.score}
Notes: {lead.notes}

Write a friendly follow-up message in less than 120 words.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert education sales assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content