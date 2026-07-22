AI PR Agent

Features
- GitHub PR analysis
- Gemini-powered summaries
- .env file configuration

Setup
1. Add secrets to `.env` file:
   Create a `.env` file in the root directory and add:
   ```
   GITHUB_TOKEN=your_github_token
   GEMINI_API_KEY=your_gemini_key
   ```

4. Run FastAPI
-> uvicorn app.main:app --reload --port 9000

Endpoints
GET /summarize-pr