from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import atlanta_trains

app = FastAPI(title="Atlanta Train Tracker API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Consider limiting this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Atlanta Train Tracker API, WIP"}

@app.get("/trains")
async def get_trains():
    return atlanta_trains.get_cached_data()
