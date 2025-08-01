from dotenv import load_dotenv
import os

load_dotenv()

train_url = os.getenv("TRAIN_URL")
prediction_url = os.getenv("PREDICTION_URL")
