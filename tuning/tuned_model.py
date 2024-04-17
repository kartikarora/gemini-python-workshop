import time

import google.generativeai as genai

from utils.utils import tuned_model_name

model = genai.GenerativeModel(model_name=f'tunedModels/{tuned_model_name}')

result = model.generate_content('Can your company help me design a building that generates its own electricity?')
print(result.text)

result = model.generate_content(
    'What is the coolest sustainable feature you have ever incorporated into a building design?')
print(result.text)

result = model.generate_content('Any tips for making my home more eco-friendly without breaking the bank?')
print(result.text)

result = model.generate_content('Can you create a building that is completely off the grid?')
print(result.text)

result = model.generate_content(
    'What is the weirdest request you have ever gotten regarding sustainable building design?')
print(result.text)
