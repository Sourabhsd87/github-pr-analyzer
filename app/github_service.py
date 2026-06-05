from github import Github
from app.config import GITHUB_TOKEN

github_client = Github(GITHUB_TOKEN)


def fetch_pr_data(repo_name: str, pr_number: int):
    repo = github_client.get_repo(repo_name)

    pr = repo.get_pull(pr_number)

    files = []
    commits = []

    for file in pr.get_files():
        files.append(
            {
                "filename": file.filename,
                "status": file.status,
                "changes": file.changes,
                "patch": file.patch,
            }
        )

    for commit in pr.get_commits():
        commits.append({"message": commit.commit.message})

    return {
        "title": pr.title,
        "description": pr.body,
        "files": files,
        "commits": commits,
    }
