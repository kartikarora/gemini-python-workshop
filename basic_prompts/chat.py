"""
Prompt:
    What are the steps to design an energy-efficient building?

Prompt:
    Who can I hire to do the first one?
"""

import google.generativeai as genai

from utils.utils import API_KEY

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('models/gemini-pro')

chat = model.start_chat()

response = chat.send_message(
    "What are the steps to design an energy-efficient building?"
)

print(response.text)

response = chat.send_message(
    "Who can I hire to do the first one?"
)

print(response.text)
