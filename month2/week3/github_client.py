import json
import requests
from pathlib import Path
import datetime

BASE_URL = "https://api.github.com"
HEADERS = {
    'Accept': 'application/vnd.github+json',
    'X-Github-Api-Version': '2022-11-28'
}

def safe_get(url , params=None, headers= None):
    try: 
        response = requests.get(
            url,
            params=params,
            headers= headers,timeout= 10
        )
        response.raise_for_status()
        return response
    except requests.exceptions.ConnectTimeout:
        print(f"Request Timed Out {url}")
        return None
    except requests.exceptions.ConnectionError:
        print(f"Connection Error {url}")
        return  None
    except requests.exceptions.HTTPError as e:
        print(f" Http error:  {response.status_code} :  {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Requests error : {e}")
        return None
    
def get_user_profile(username):
    url = f"BASE_URL/users/{username}"
    response = safe_get(url, headers=HEADERS)
    if not response:
        return None
    user = response.json()
    return  {
        'username' : user['login'],
        'name':user.get('name') or 'Not set',
        'bio': user.get['bio'] or 'No bio',
        'location':user.get['location'] or 'Not set',
        'public_repos':user['public_repos'],
        'followers':user['followers'],
        'following':user['following'],
        'profile_url':user['profile_url'],
        'created_at':user['created_at']
    }