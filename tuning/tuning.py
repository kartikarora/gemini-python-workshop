import json
import time

import google.generativeai as genai
from google.generativeai.types import TunedModelState

from utils.utils import tuned_model_name

training_data_file = open('../assets/training_data.json', 'r')
training_data = json.load(training_data_file)
training_data_file.close()

base_model = [
    model for model in genai.list_models()
    if "createTunedModel" in model.supported_generation_methods][0]


operation = genai.create_tuned_model(
    source_model=base_model.name,
    training_data=training_data,
    id=tuned_model_name,
    epoch_count=100,
    batch_size=4,
    learning_rate=0.001,
)
model = genai.get_tuned_model(f'tunedModels/{tuned_model_name}')
state = model.state

for status in operation.wait_bar():
    if status is not TunedModelState.ACTIVE:
        time.sleep(1)
    else:
        break

if state is TunedModelState.ACTIVE:
    print(f"Model {tuned_model_name} is ready for use")
