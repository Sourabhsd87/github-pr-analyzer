import json
import logging

import app.logging_config  # noqa: F401 — configure logging before other app imports

from fastapi import FastAPI, HTTPException

from app.github_service import fetch_pr_data
from app.prompt_builder import build_pr_summary_prompt
from app.ai_service import generate_summary

logger = logging.getLogger(__name__)

app = FastAPI(
    title="PR Summary Agent",
    description="AI-powered GitHub Pull Request Analysis Tool",
    version="1.0.0",
)


@app.on_event("startup")
def on_startup():
    logger.info("PR Summary Agent started")


@app.get("/summarize-pr")
def summarize_pr(repo: str, pr_number: int):
    logger.info("Summarize PR request received for %s#%s", repo, pr_number)

    pr_data = fetch_pr_data(repo, pr_number)
    logger.debug(
        "Fetched PR data: title=%r, files=%d, commits=%d",
        pr_data.get("title"),
        len(pr_data.get("files", [])),
        len(pr_data.get("commits", [])),
    )

    prompt = build_pr_summary_prompt(pr_data)
    logger.debug("Built prompt (%d characters)", len(prompt))

    summary = generate_summary(prompt)
    logger.debug("Received AI response (%d characters)", len(summary))

    try:
        parsed_response = json.loads(summary)
    except json.JSONDecodeError as exc:
        logger.error(
            "Failed to parse AI response as JSON for %s#%s: %s",
            repo,
            pr_number,
            exc,
        )
        raise HTTPException(
            status_code=502,
            detail="AI returned invalid JSON",
        ) from exc

    logger.info("Successfully summarized %s#%s", repo, pr_number)
    return parsed_response
