# Load enviroment
import os
from dotenv import load_dotenv

MODEL_1 = "gpt-5-nano"
MODEL_2 = "gpt-4.1-mini"
MODEL_3 = "gpt-4o-mini"
FAV_ICON_URL = "/assets/favicon.png"

def load_environment():
    load_dotenv(override=True)
    api_key = os.getenv('OPENAI_API_KEY')   
    return api_key


