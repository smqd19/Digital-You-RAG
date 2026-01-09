import os
import glob
from dotenv import load_dotenv

# Verified Modern LangChain Imports
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

import gradio as gr

# 1. Environment Configuration, should have a .env file with API Key
load_dotenv(override=True)

def ingest_data():
    """
    Task 1: Data Ingestion Pipeline
    Scan the 'data/' folder for markdown files and load them into Documents.
    """
    file_paths = glob.glob("data/**/*.md", recursive=True)
    if not file_paths:
        return [Document(page_content="I am a professional twin.", metadata={"source": "none"})]
    
    documents = []
    for path in file_paths:
        with open(path, "r", encoding="utf-8") as f:
            documents.append(Document(page_content=f.read(), metadata={"source": path}))
    return documents

def initialize_modern_rag():
    """
    Task 2: RAG Orchestration Setup
    """
    # A. Load and Split Documents
    docs = ingest_data()
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    
    # TODO: Milestone 1 - Implement the RecursiveCharacterTextSplitter
    splitter = None 
    chunks = [] 
    
    # B. Vector Storage
    # TODO: Milestone 2 - Initialize Chroma vectorstore and create a retriever
    vectorstore = None
    retriever = None
    
    # C. Language Model Initialization
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # --- PART A: History Management ---
    # TODO: Milestone 3 - Define the 'contextualize_q_prompt'
    # Use MessagesPlaceholder("chat_history") and the human input.
    contextualize_q_prompt = None
    
    # TODO: Milestone 4 - Create the history_aware_retriever
    history_aware_retriever = None

    # --- PART B: Answer Question (Persona & Context) ---
    # TODO: Milestone 5 - WRITE YOUR OWN PERSONA PROMPT
    # Instructions: You MUST define who you are, how you should answer, 
    # and ensure the AI uses the provided {context} and {chat_history}.
    qa_prompt = None
    
    # TODO: Milestone 6 - Create the question_answer_chain (Stuff Documents)
    question_answer_chain = None
    
    # --- PART C: Final RAG Chain ---
    # TODO: Milestone 7 - Combine Parts A and B into a final chain
    return None 

# Initialize global components
rag_chain = initialize_modern_rag()
stateful_history = [] 

def chat_handler(message, history):
    global stateful_history
    
    # TODO: Milestone 8 - Invoke the rag_chain with 'input' and 'chat_history'
    # Use: response = rag_chain.invoke({"input": message, "chat_history": stateful_history})
    response = {"answer": "I am waiting for you to complete the implementation in app.py!"}
    
    # Update stateful history
    stateful_history.append(("human", message))
    stateful_history.append(("assistant", response["answer"]))
    
    return response["answer"]

# 3. UI Implementation
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🤖 Project 2: RAG Orchestrator")
    gr.ChatInterface(fn=chat_handler, type="messages")

if __name__ == "__main__":
    demo.launch()