from bs4 import BeautifulSoup
import requests
import json

SONG_URLS = "https://us.millenium.gg/news/25575.html"
FILE_NAME = "stations.json"

def get_station_song(soup: BeautifulSoup) -> dict[str, str]:
    stations = {}
    for station in soup.find_all('h2', class_="article__subtitle"):
        songs = station.next_sibling.next_sibling.children
        songs = [song for song in songs if song != '\n']
        stations[station.text] = [song.text for song in songs]

    return stations

def get_station_dj(stations_songs: dict[str, str]) -> list[list[str]]:
    stations = list(stations_songs.keys())
    station_dj = [station.split("|") for station in stations]
    return station_dj

def create_artist_song_pair(artist_song_pairs):
    songs = []
    for pair in artist_song_pairs:
        # some radio stations talk only, no songs
        if len(pair) == 2:
            artist_song = {"artist": pair[0], "song": pair[1]}
        else:
            artist_song = {"artist": pair[0], "song": pair[0]}

        songs.append(artist_song)
    return songs

def create_station_schema(stations_songs, station_djs):
    schema = []
    for pair in station_djs:
        station = pair[0]
        dj = pair[1]

        og_key = " | ".join([station, dj]) 
        dj = dj.split(":")[1].strip()

        songs = stations_songs[og_key]
        artist_song_pairs = [single.split(" - ") for single in songs]
        songs = create_artist_song_pair(artist_song_pairs)

        schema.append({"station_name": station, 'dj': dj, 'songs': songs})

    return schema

def clean_whitespace(l: list):
    if not l:
        return
    
    if isinstance(l, str):
        l = l.strip()
        return l
    
    for i, item in enumerate(l):
        item = clean_whitespace(item)
        if item is not None:
            l[i] = item

def write_to_json(schema: dict, file_name: str):
    json_obj = json.dumps(schema, indent=4, sort_keys=True)

    with open(file_name, 'w') as f:
        f.write(json_obj)

def main():
    html = requests.get(SONG_URLS)
    soup = BeautifulSoup(html.text, 'html.parser')

    stations_songs = get_station_song(soup)
    station_djs = get_station_dj(stations_songs)
    clean_whitespace(station_djs)

    schema = create_station_schema(stations_songs, station_djs)    
    schema = {"stations": schema}
    write_to_json(schema, FILE_NAME)

if __name__ == "__main__":
    main()