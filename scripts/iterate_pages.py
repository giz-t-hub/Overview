import requests
import base64
import os

# List of repository URLs categorized by continent
repos_by_continent = {
    "Europe": [
        "https://github.com/giz-t-hub/Albania",
        "https://github.com/giz-t-hub/Armenia",
        "https://github.com/giz-t-hub/Azerbaijan",
        "https://github.com/giz-t-hub/BosniaandHerzegovina",
        "https://github.com/giz-t-hub/Croatia",
        "https://github.com/giz-t-hub/Georgia",
        "https://github.com/giz-t-hub/Germany",
        "https://github.com/giz-t-hub/Kosovo",
        "https://github.com/giz-t-hub/Moldova",
        "https://github.com/giz-t-hub/Montenegro",
        "https://github.com/giz-t-hub/NorthMacedonia",
        "https://github.com/giz-t-hub/Poland",
        "https://github.com/giz-t-hub/Serbia",
        "https://github.com/giz-t-hub/Ukraine",
    ],
    "Asia": ["https://github.com/giz-t-hub/India"],
    "Africa": [
        "https://github.com/giz-t-hub/Kenya",
        "https://github.com/giz-t-hub/Rwanda",
    ],
    "Latin America": [
        "https://github.com/giz-t-hub/Argentina",
        "https://github.com/giz-t-hub/Brazil",
        "https://github.com/giz-t-hub/Chile",
        "https://github.com/giz-t-hub/Colombia",
        "https://github.com/giz-t-hub/Costa-Rica",
        "https://github.com/giz-t-hub/Ecuador",
        "https://github.com/giz-t-hub/Mexico",
        "https://github.com/giz-t-hub/Peru",
    ],
}


def get_repo_readme(repo_url):
    # Extract owner and repo name from URL
    parts = repo_url.split("/")
    owner, repo = parts[-2], parts[-1]

    # GitHub API URL to get README.md
    api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"

    # GitHub API request
    response = requests.get(api_url)

    if response.status_code == 200:
        readme_data = response.json()
        readme_content = base64.b64decode(readme_data["content"]).decode("utf-8")
        return readme_content
    else:
        print(f"Failed to get README.md for {repo}")
        return None


def save_readme_to_file(continent, repo, readme_content):
    # Create continent directory if it does not exist
    if not os.path.exists(f'transport-docs-handbook/documents/{continent}'):
        os.makedirs(f'transport-docs-handbook/documents/{continent}')

    # Extract repo name from URL
    repo_name = repo.split("/")[-1]

    # Define file path
    file_path = os.path.join(
        "transport-docs-handbook/documents", continent, f"{repo_name}_README.md"
    )

    # Save README.md content to file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(readme_content)


# Loop through each continent and their respective repository URLs
for continent, repos in repos_by_continent.items():
    for repo in repos:
        readme = get_repo_readme(repo)
        if readme:
            save_readme_to_file(continent, repo, readme)

print("README.md files have been saved to respective continent folders.")
