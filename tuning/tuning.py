import json
import time

import google.generativeai as genai
from google.generativeai.types import TunedModelState

from utils.utils import tuned_model_name

training_data_file = open('../assets/training_data.json', 'r')
training_data = json.load(training_data_file)
training_data_file.close()
