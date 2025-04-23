import os
from fastapi import FastAPI
from langchain_community.vectorstores import Pinecone as LangchainPinecone
from langchain_community.embeddings import OpenAIEmbeddings
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

# Connect to index (no need to create here unless necessary)
index = pc.Index(PINECONE_INDEX)

# Set up embeddings
embeddings = OpenAIEmbeddings()

# Wrap index for LangChain
vectorstore = LangchainPinecone(index, embeddings, "metadata")

# Create FastAPI app
app = FastAPI()

@app.get("/get-error-response")
def get_error_response():
    return {"message": "Your support API is working!"}
