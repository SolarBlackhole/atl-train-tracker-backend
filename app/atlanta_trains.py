import requests
import threading
import time
from . import links

cache = {
    "trains": [],
    "predictions": [],
    "last_updated": None
}

def poll_train_api():
    while True:
        try:
            trains = requests.get(links.train_url).json()
            predictions = requests.get(links.prediction_url).json()
            cache["trains"] = trains
            cache["predictions"] = predictions
            cache["last_updated"] = time.time()
        except Exception as e:
            print(f"[ERROR] Polling failed: {e}")
        time.sleep(10)

def get_cached_data():
    return cache

# Start background polling
threading.Thread(target=poll_train_api, daemon=True).start()
