"""
Prompt:
    What are the benefits of using energy-efficient lighting in buildings?
"""

import google.generativeai as genai

from utils.utils import API_KEY

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('models/gemini-pro')

response = model.generate_content(
    'What are the benefits of using energy-efficient lighting in buildings?'
)

print(response.text)
