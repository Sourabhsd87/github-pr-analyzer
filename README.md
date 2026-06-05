AI PR Agent

Features
- GitHub PR analysis
- Gemini-powered summaries
- Vault-based secret management

Setup
1. Start Vault
-> docker exec -it vault sh

2. Add GitHub token
-> vault kv put secret/github token="your_github_token"

3. Add Gemini API key
-> vault kv put secret/gemini api_key="your_gemini_key"

4. Run FastAPI
-> uvicorn app.main:app --reload --port 9000

Endpoints
GET /summarize-pr