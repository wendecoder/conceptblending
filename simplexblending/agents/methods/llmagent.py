from openai import OpenAI
from hyperon import *

openai = OpenAI()
def call_openai(metta: MeTTa, *args, model="gpt-4-turbo", max_tokens=100):
    prompt = args[0]
    try:
        response = openai.Completion.create(
            engine=model,  
            prompt=prompt,  
            max_tokens=max_tokens,  
            temperature=0.7,
        )
        return response['choices'][0]['text'].strip()
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"