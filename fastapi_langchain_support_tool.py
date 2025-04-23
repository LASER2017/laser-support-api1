from fastapi import FastAPI
from pydantic import BaseModel
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import pinecone
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
embedding = OpenAIEmbeddings()
index = Pinecone.from_existing_index(PINECONE_INDEX, embedding)
retriever = index.as_retriever()
qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(), retriever=retriever)

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/get-error-response")
async def get_error_response(data: QueryRequest):
    try:
        response = qa.run(data.query)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def root():
    return {"message": "LASER Support GPT Vector Search API is running."}