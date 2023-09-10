# Vice City API
"It's Lazlow on V-ROCK!"

<p align="center">
  <img src="https://github.com/kostyafarber/vice-city-api/assets/73378227/7d8f906f-baab-4ac7-ae50-0b56cc5e34d1"/>
</p>

## Docmentation
https://vice-city-api-kostyafarber.koyeb.app/docs
## Usage
### Local 
To install the app locally
```shell
uvicorn api.router:app --reload
```

### All stations
```shell
curl -X GET http://127.0.0.1:8000/stations/
```
### Specific station
```shell
curl -X GET http://127.0.0.1:8000/stations/K-Chat
```

## Live
https://vice-city-api-kostyafarber.koyeb.app/

### All Stations
https://vice-city-api-kostyafarber.koyeb.app/stations/

```json
{
  "stations": [
    {
      "dj": "Adam First (Jamie Canfield)",
      "songs": [
        {
          "artist": "Frankie Goes to Hollywood",
          "song": "Two Tribes"
        },
        {
          "artist": "Tears For Fears",
          "song": "Pale Shelter"
        },
        {
          "artist": "Kim Wilde",
          "song": "Kids in America"
        },
        {
          "artist": "Blondie",
          "song": "Atomic"
        },
        {
          "artist": "A Flock of Seagulls",
          "song": "I Ran (So Far Away)"
        },
        {
          "artist": "The Human League",
          "song": "(Keep Feeling) Fascination"
        },
        {
          "artist": "Nena",
          "song": "99 Luftballoons"
        },
        {
          "artist": "The Psychedelic Furs",
          "song": "Love My Way"
        },
        {
          "artist": "Spandau Ballet",
          "song": "Gold"
        },
        {
          "artist": "Thomas Dolby",
          "song": "Hyperactive!"
        },
        {
          "artist": "Romeo Void",
          "song": "Never Say Never"
        },
        {
          "artist": "Corey Hart",
          "song": "Sunglasses at Night"
        }
      ],
      "station_name": "Wave 103"
    },
    .
    .
    .
```
### Specific station
https://vice-city-api-kostyafarber.koyeb.app/stations/V-Rock

```json
{
  "dj": "Lazlow (voiced by himself)",
  "songs": [
    {
      "artist": "Judas Priest",
      "song": "You've Got Another Thing Coming"
    },
    {
      "artist": "Motley Crue",
      "song": "Too Young to Fall in Love"
    },
    {
      "artist": "Megadeth",
      "song": "Peace Sells"
    },
    {
      "artist": "Rockstar's Lovefist",
      "song": "Dangerous Bastard"
    },
    {
      "artist": "Autograph",
      "song": "Turn Up the Radio"
    },
    {
      "artist": "Twisted Sister",
      "song": "I Wanna Rock"
    },
    {
      "artist": "Anthrax",
      "song": "Madhouse"
    },
    {
      "artist": "Iron Maiden",
      "song": "2 Minutes to Midnight"
    },
    {
      "artist": "Slayer",
      "song": "Raining Blood"
    },
    {
      "artist": "Tesla",
      "song": "Comin 'Atcha Live"
    },
    {
      "artist": "David Lee Rose",
      "song": "Yankee Rose"
    }
  ],
  "station_name": "V-Rock"
}
```

