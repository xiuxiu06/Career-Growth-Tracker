import openai
import os

openai.api_key = "sk-...ECMA"

def get_skill_recommendations(job_title):
    prompt = f"What are the top skills required for a {job_title}?"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]
