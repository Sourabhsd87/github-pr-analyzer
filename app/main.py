import json

from fastapi import FastAPI

from app.github_service import fetch_pr_data
from app.prompt_builder import build_pr_summary_prompt
from app.ai_service import generate_summary

app = FastAPI()


@app.get("/summarize-pr")
def summarize_pr(repo: str, pr_number: int):

    pr_data = fetch_pr_data(repo, pr_number)

    prompt = build_pr_summary_prompt(pr_data)

    summary = generate_summary(prompt)

    parsed_response = json.loads(summary)

    return parsed_response