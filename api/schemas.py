from pydantic import BaseModel
import json

class Single(BaseModel):
    artist: str
    song: str

class Station(BaseModel):
    dj: str
    songs: list[Single]
    station_name: str

class Stations(BaseModel):
    stations: list[Station]

if __name__ == "__main__":
    with open("../data/stations.json") as f:
        stations_json = json.load(f)
    
    stations_model = Stations(**stations_json)
    print(stations_model) 