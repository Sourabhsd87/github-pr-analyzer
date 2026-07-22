import logging

from github import Github

from app.config import GITHUB_TOKEN

logger = logging.getLogger(__name__)

github_client = Github(GITHUB_TOKEN)

from fastapi import HTTPException
from github.GithubException import UnknownObjectException, RateLimitExceededException, GithubException

def fetch_pr_data(repo_name: str, pr_number: int):
    logger.info("Fetching PR data for %s#%s", repo_name, pr_number)

    try:
        repo = github_client.get_repo(repo_name)
        pr = repo.get_pull(pr_number)

        files = []
        for file in pr.get_files():
            files.append(
                {
                    "filename": file.filename,
                    "status": file.status,
                    "changes": file.changes,
                    "patch": file.patch,
                }
            )

        commits = [{"message": c.commit.message} for c in pr.get_commits()]

        logger.info(
            "Fetched PR %s#%s: %d files, %d commits",
            repo_name,
            pr_number,
            len(files),
            len(commits),
        )

        return {
            "title": pr.title,
            "description": pr.body,
            "files": files,
            "commits": commits,
        }
    except UnknownObjectException:
        logger.error("Repository or PR not found: %s#%s", repo_name, pr_number)
        raise HTTPException(status_code=404, detail="Repository or Pull Request not found")
    except RateLimitExceededException:
        logger.error("GitHub API rate limit exceeded")
        raise HTTPException(status_code=429, detail="GitHub API rate limit exceeded")
    except GithubException as e:
        logger.error("GitHub API error: %s", getattr(e, 'data', e))
        raise HTTPException(status_code=502, detail="Error communicating with GitHub")
