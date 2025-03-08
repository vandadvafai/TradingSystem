import os
from dotenv import load_dotenv

load_dotenv()  

SIMFIN_API_KEY = os.getenv("SIMFIN_API_KEY")
if SIMFIN_API_KEY is None:
    raise ValueError("No SimFin API key found in environment variables!")
