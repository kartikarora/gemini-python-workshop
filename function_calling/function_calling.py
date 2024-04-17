"""
Prompt

    There is s a building which uses about 10000 kWh of energy. The energy price is roughly $0.12 per kWh. There is a
    discount of 1% on the energy price for using energy efficient measures, which themselves are 80% efficient. What
    would be the total energy savings in this case?
"""

import google.generativeai as genai
from utils.energy_savings import calculate_total_energy_savings

from utils.utils import API_KEY

genai.configure(api_key=API_KEY)
