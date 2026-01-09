# Digital Twin - RAG Evolution

Earlier we utilized "Context Stuffing" to create the Digital You. This project evolves that concept into a **Retrieval Augmented Generation (RAG)** system for better scalability and efficiency.

## Architectural Evolution

1. **Ingestion**: Reads documents from `/data`.
2. **Chunking**: Splits text into manageable segments.
3. **Embedding**: Converts text into numerical vectors.
4. **Retrieval**: Fetches only relevant segments to answer user queries.

## Setup

1. **Sync Environment**: `uv sync` in the root directory.
2. **Data**: Place .txt, .md, or .pdf files in the `/data` directory.
3. **Tasks**: Complete the TODOs in `app.py` to build the RAG pipeline.

## Your Mission

1. **Data Infrastructure**: Build a vector store in `chroma_db/` using your bio data.
2. **Contextualization**: Teach the AI how to re-write questions based on history so it never "forgets" the subject of conversation.
3. **Persona Engineering**: You must write your own `qa_prompt`. This is where you define your "Digital Twin" identity and force the AI to only use the retrieved context.

## Enhancements

- Use `SemanticChunker` for smarter context splitting.
- Customize the Gradio UI using `gr.Blocks`.
