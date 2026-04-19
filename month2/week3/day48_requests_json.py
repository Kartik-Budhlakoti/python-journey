import json 
from pathlib import Path
import requests

def safe_get(url,headers=None, params=None):
    try:
        response = requests.get(url , headers=headers, params=params, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request failed : {e}")
        return None

def save_json(data, filepath):
    """Save any data in the formatted Json file ."""
    path = Path(filepath)
    path.write_text(json.dumps(data, indent=4))
    print(f"Saved to: {path}")

def load_json(filepath):
    path = Path(filepath)
    if not path.exists():
        print(f"File not found : {filepath}")
        return None
    return json.loads(path.read_text())


headers = {'Accept': 'application/json'}
response = safe_get('https://wttr.in/Dehradun', params= {'format': 'j1'})

# for the entir response ----
# user = response.json()
# print(f"json response: {json.dumps(user, indent=4)}")

if response:
    weather_data = response.json()

    # saving raw data
    save_json(weather_data, '/home/kartik007/Desktop/python-new/python-journey/month2/week3/weather_raw.json')

    #  Extarcting only what we need and saving a clean version
    current = weather_data['current_condition'][0]
    clean_data = {
        'location':'Dehradun',
        "temperature_c": current['temp_C'],
        'feels_like': current['FeelsLikeC'],
        'humidity': current['humidity'],
        'description': current['weatherDesc'][0]['value'],
        'wind_speed_kmph': current['windspeedKmph']
    }
    save_json(clean_data, '/home/kartik007/Desktop/python-new/python-journey/month2/week3/weather_clean.json')

    # load it back and display
    loaded = load_json('/home/kartik007/Desktop/python-new/python-journey/month2/week3/weather_clean.json')
    if loaded:
        print(f"\n\n Weather in {loaded['location']} : ")
        print(f"   Temperature : {loaded['temperature_c']} degree CELCIUS")
        print(f"   Feels like: {loaded['feels_like']} degree CELCIUS")
        print(f"   Humidity : {loaded['humidity']}%")
        print(f"   Condition : {loaded['description']} and the Wind speed is : {loaded['wind_speed_kmph']}kmph")