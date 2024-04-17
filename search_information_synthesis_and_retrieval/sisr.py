"""
Prompt:
    How does your company ensure that sustainable building designs align with client objectives?
"""

import pathlib
import google.generativeai as genai

from utils.utils import API_KEY

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('models/gemini-pro')





