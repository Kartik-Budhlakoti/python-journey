import requests

print('==== Basic Get Request ====')
response= requests.get('https://httpbin.org/get')

print(f" Status Code : {response.status_code}")
print(f"Response Type: {response.encoding} and {type(response)}")
print(f" Content Type: {response.headers.get('Content-Type')}")

data = response.text
print(f"Your IP address : {data}")
data = response.json()
print(f"Your IP address : {data['origin']}")

# Get with parameters
response = requests.get(
    "https://httpbin.org/get",
    params={'name': 'kartik','city': 'dehradun'}
)
data = response.json()
print(f"Parameters sent: {data["args"]}")

print(f"\n=== ERROR HANDLING ===")
def safe_get(url, params=None):
    # making get requests with error handling
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.Timeout:
        print(f"Request Timed out: {url}")
        return None
    except requests.exceptions.ConnectionError:
        print(f"Connection Failed: {url}")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Http error {response.status_code}: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request Failed: {e}")
        return None
    
# testing with valid url
response = safe_get('https://httpbin.org/get')
if response:
    print(f"Success: {response.status_code}")
# now with invalid url
response = safe_get('https://httpbin.org/status/404')
if not response:
    print("Handled 404 Gracefully")
# now the timeout error
response = safe_get("https://httpbin.org/delay/15")
if not response:
    print('Handled Timeout Gracefully')

print(f"\n === Weather API === ")
response = safe_get("https://wttr.in/Dehradun", params={'format': 'j1'})
if response:
    weather = response.json()
    # Navigate nested JSON - whether is a Dictionary or Dictionaries
    current = weather['current_condition'][0]
    temp_c = current['temp_C']
    feels_like = current['FeelsLikeC']
    description = current['weatherDesc'][0]['value']
    print(f"Dehradun whether: {description}")
    print(f"Temperature: {temp_c} Celcius")
    print(f"Feels like: {feels_like} degree Celcius")