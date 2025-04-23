# LASER Support GPT API

FastAPI + LangChain + Pinecone API for responding to credit error messages.

## Deploy to Render

1. Upload this repo to GitHub.
2. On Render, create a new Web Service linked to your repo.
3. Set:
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn fastapi_langchain_support_tool:app --host 0.0.0.0 --port 10000`
4. Add env vars for OPENAI_API_KEY, PINECONE_API_KEY, PINECONE_ENV, and PINECONE_INDEX.