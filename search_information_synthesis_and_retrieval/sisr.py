"""
Prompt:
    How does your company ensure that sustainable building designs align with client objectives?
"""

import pathlib
import google.generativeai as genai

from utils.utils import API_KEY

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('models/gemini-pro')

document_correct = pathlib.Path('../assets/document_correct.txt').read_text()
document_wrong = pathlib.Path('../assets/document_wrong.txt').read_text()

result_correct = model.generate_content(f"""
  How does your company ensure that sustainable building designs align with client objectives?

  Please answer based on the following document:
  {document_correct}""")

print(result_correct.text)

result_wrong = model.generate_content(f"""
  How does your company ensure that sustainable building designs align with client objectives?

  Please answer based on the following document:
  {document_wrong}""")

print(result_wrong.text)
