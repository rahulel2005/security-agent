import os
import requests


GITHUB_API = "https://api.github.com"


def get_repo_info():
    repo = os.getenv("GITHUB_REPOSITORY")
    if not repo or "/" not in repo:
        raise ValueError("GITHUB_REPOSITORY not found")
    owner, name = repo.split("/", 1)
    return owner, name


def get_headers():
    token = os.getenv("GITHUB_TOKEN_CUSTOM")
    if not token:
        raise ValueError("GITHUB_TOKEN_CUSTOM not found")
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }


def create_pull_request(branch_name, title, body, base="main"):
    owner, repo = get_repo_info()
    url = f"{GITHUB_API}/repos/{owner}/{repo}/pulls"

    payload = {
        "title": title,
        "head": branch_name,
        "base": base,
        "body": body
    }

    response = requests.post(url, headers=get_headers(), json=payload, timeout=30)
    response.raise_for_status()
    return response.json()