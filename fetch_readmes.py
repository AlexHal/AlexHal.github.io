import requests
import base64
import json
import os

# GitHub username and token (optional if private repositories are included)
GITHUB_USERNAME = "AlexHal"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPOS_FILE = "repos.txt"
OUTPUT_FILE = "_data/repos.json"

headers = {
    "Accept": "application/vnd.github.v3+json",
}

if GITHUB_TOKEN:
    headers["Authorization"] = f"token {GITHUB_TOKEN}"


def fetch_readme(repo_name):
    full_repo_name = f"{GITHUB_USERNAME}/{repo_name}"
    url = f"https://api.github.com/repos/{full_repo_name}/readme"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        readme_data = response.json()
        content = base64.b64decode(readme_data["content"]).decode("utf-8")
        return content
    return None


def main():
    if not os.path.exists(REPOS_FILE):
        print(f"{REPOS_FILE} not found!")
        return

    repos = []
    with open(REPOS_FILE, "r") as file:
        for line in file:
            repo_name = line.strip()
            if repo_name:
                print(f"Fetching README for {repo_name}...")
                readme = fetch_readme(repo_name)
                repos.append({
                    "name": repo_name,
                    "html_url": f"https://github.com/{GITHUB_USERNAME}/{repo_name}",
                    "readme": readme or "README not available",
                })

    os.makedirs("_data", exist_ok=True)
    with open(OUTPUT_FILE, "w") as json_file:
        json.dump(repos, json_file, indent=2)
        print(f"Saved repository data to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
