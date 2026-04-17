import requests
import json

def safe_get(url, headers=None):
    try: 
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request Failed : {e}")
        return None

# Github API requires this header
headers = {
    'Accept': 'application/vnd.github+json',
    'X-Github-Api-Version': '2022-11-28'
}
url = 'https://api.github.com/users/Kartik-Budhlakoti'
response = safe_get(url, headers=headers)
if response:
    user = response.json()
    print(f"Username: {user['login']}")
    print(f"Name: {user.get('name', 'Notset')}")
    print(f"Public repos: {user['public_repos']}")
    print(f"Followers: {user['followers']}")
    print(f"Following: {user['following']}")

    #  Now printing raw json for better understanding its structure
    print(f"\n==== Raw Json Structure ===")
    print(json.dumps(user, indent=4))