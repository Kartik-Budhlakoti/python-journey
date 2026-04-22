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
    url = f"{BASE_URL}/users/{username}"
    response = safe_get(url, headers=HEADERS)
    if not response:
        return None
    user = response.json()
    return  {
        'username' : user['login'],
        'name':user.get('name') or 'Not set',
        'bio': user.get('bio') or 'No bio',
        'location':user.get('location') or 'Not set',
        'public_repos':user['public_repos'],
        'followers':user['followers'],
        'following':user['following'],
        'profile_url':user['html_url'],
        'created_at':user['created_at']
    }
def get_repositories(username):
    url = f"{BASE_URL}/users/{username}/repos"
    response = safe_get(url, headers=HEADERS,
                        params={'sort':'updated', 'per_page':'100'})
    if not response:
        return []
    repos = response.json()
    clean_repos = []
    for repo in repos:
        clean_repos.append({
            'name': repo['name'],
            'description':repo.get('description') or 'No description',
            'language': repo.get('language') or 'Not specified',
            'stars': repo['stargazers_count'],
            'forks': repo['forks_count'],
            'updated_at': repo['updated_at'],
            'url': repo['html_url'],
            'is_fork':repo['fork']
        })
        return clean_repos

def get_recent_commit(username, repo_name, count=5):
    url = f"{BASE_URL}/repos/{username}/{repo_name}/commits"
    response = safe_get(
        url,
        headers=HEADERS,
        params={'per_page':count}
    )
    if not response:
        return []
    
    commits = response.json()

    # Checking if the output response is actually a list or not  -------------------------------------
    # error that github gives as a dictionary instead of list  ---------------------
    if not isinstance(commits, list):
        return []

    clean_commits = []
    for commit in commits:
        clean_commits.append({
            #   first 7 chars of commit hash
            'sha': commit['sha'][:7],
            #  1st line only
            'message': commit['commit']['message'].split('\n')[0],
            'author':commit['commit']['author']['name'],
            'date':commit['commit']['author']['date']
        })
        
    return clean_commits
def display_profile(profile):
    if not profile:
        print(f"Could not load profile")
        return 
    print(f"=" *50)
    print('Github Profile---')
    print('='*50)
    print(f"Username : {profile['username']}")
    print(f"Name : {profile['name']}")
    print(f"Bio : {profile['bio']}")
    print(f"Location : {profile['location']}")
    print(f"Repos : {profile['public_repos']}")
    print(f"Followers : {profile['followers']}")
    print(f"Following : {profile['following']}")
    print(f"Url : {profile['profile_url']}")

def display_repositories(repos):
    if not repos:
        print(f"No repos were found")
        return 
    print(f"="*50)
    print(f"Repositories : {len(repos)} total")
    print("="*50)

    original = [r for r in repos if not r['is_fork']]
    forks = [r for r in repos if r['is_fork']]    

    print(f"Original : {len(original)} | Forks : {len(forks)}")
    print()

    for repo in repos[:10]:#   for first 10 repos
        fork_label = " [FORK]" if repo['is_fork'] else ""
        print(f"  {repo['name']}{fork_label}")
        print(f"   {repo['description']}")
        print(f"    Language : {repo['language']} | Starts : {repo['stars']}")
        print()

def display_commits(commits, repo_name):
    if not commits:
        print("No commits to display for {repo_name}")
        return 
    print(f"="*50)
    print(f"Latest commits for : {repo_name}")
    print("="*50)
    for commit in commits:
        print(f"    [{commit['sha']}] {commit['message']}")
        print(f"        by {commit['author']} on {commit['date'][:10]}")
        print()
def save_data(profile, repos, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True, parents=True)

    timestamp = datetime.datetime.now().strftime('%Y:%m:%d_%H:%M:%S')

    #save profile
    profile_file = output_path / f"profile_{timestamp}.json"
    profile_file.write_text(json.dumps(profile, indent=4))
    print(f" Profile Information saved in : {profile_file}")

    #save repos
    repos_file = output_path / f"repos_{timestamp}.json"
    repos_file.write_text(json.dumps(repos, indent= 4))
    print(f" Repositories Information saved in  : {repos_file}")
    return str(profile_file) ,str(repos_file)

def main():
    username= "Kartik-Budhlakoti"
    output_dir = "/home/kartik007/Desktop/python-new/python-journey/month2/week3/github_data"

    profile = get_user_profile(username)
    display_profile(profile)

    repos = get_repositories(username)
    display_repositories(repos)

    if repos:
        most_recent_repo = repos[0]['name']
        commits = get_recent_commit(username, most_recent_repo , count=5)
        display_commits(commits, most_recent_repo)

    # now saving everything
    if profile and repos:
        save_data(profile, repos, output_dir)

    print("------     DONE     ------")

if __name__ == "__main__":
    main()