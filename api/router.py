from fastapi import FastAPI
from api.schemas import Stations, Station
import json
import os

dirname = os.path.dirname(__file__)
data = os.path.join(dirname, os.pardir, 'data/stations.json')
with open(data) as f:
    stations_json = json.load(f)

app = FastAPI()

@app.get("/stations/")
async def get_stations() -> Stations:
    return stations_json

@app.get('/stations/{station_name}', status_code=200) 
async def get_specific_station(station_name: str) -> Station:
    stations = stations_json["stations"]
    return next(station for station in stations if station["station_name"] == station_name)
