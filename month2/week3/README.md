# Week 7 — requests, json, APIs

## What I learned
- Making HTTP GET requests using the requests library
- Handling API errors gracefully with try/except
- Parsing and navigating JSON responses
- Reading and writing JSON files
- Working with the GitHub REST API

## Files
- `day45_requests.py` — requests basics, httpbin practice, weather API
- `day46_github_explore.py` — exploring GitHub API structure
- `day47_json.py` — json module, reading/writing files
- `day48_requests_json.py` — combining requests and json
- `github_client.py` — main project, GitHub API client

## How to run

```bash
# Activate venv first
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the GitHub client
python github_client.py
```

## Output
The client saves profile and repository data as JSON files in `github_data/`

## APIs used
- GitHub REST API — https://docs.github.com/en/rest
- wttr.in — free weather API
- httpbin.org — HTTP testing service