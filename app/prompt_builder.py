import logging

logger = logging.getLogger(__name__)


def build_pr_summary_prompt(pr_data: dict):
    file_count = len(pr_data["files"])
    commit_count = len(pr_data["commits"])
    patch_count = min(file_count, 10)

    logger.info(
        "Building prompt for PR %r (%d files, %d commits, %d patches included)",
        pr_data.get("title"),
        file_count,
        commit_count,
        patch_count,
    )

    changed_files = "\n".join([f"- {f['filename']}" for f in pr_data["files"]])

    commit_messages = "\n".join([f"- {c['message']}" for c in pr_data["commits"]])

    patches = "\n\n".join(
        [
            f"""
            FILE: {f['filename']}

            PATCH:
            {f['patch']}
            """
            for f in pr_data["files"][:10]
        ]
    )

    prompt = f"""
You are a senior software engineer.

Analyze this Pull Request.

PR Title:
{pr_data['title']}

PR Description:
{pr_data['description']}

Changed Files:
{changed_files}

Commit Messages:
{commit_messages}

Code Changes:
{patches}

Return ONLY valid JSON.

Expected JSON format:

{{
    "short_summary": "string",

    "file_wise_changes": [
        {{
            "file_name": "string",
            "changes": [
                "string",
                "string"
            ]
        }}
    ],

    "text to be added in CHANGELOG.md": "string",
    
    "risks": [
        "string"
    ],

    "testing_impact": [
        "string"
    ],

    "reviewer_concerns": [
        "string"
    ]
}}

Rules:
- Return only JSON
- No markdown
- No explanation
- No code block
- Mention actual file names
- Explain file-level key changes clearly
- Ensure valid parsable JSON
"""
    logger.debug("Prompt built (%d characters)", len(prompt))
    return prompt
