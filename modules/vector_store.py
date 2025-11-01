from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS 
from dotenv import load_dotenv

load_dotenv()

# create chunks for embedding 
def create_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 100,
        length_function = len
    )

    return text_splitter.create_documents([text]) # .split_text could also be used but for RAG .create_documents is used


# create embeddings of the chunks created
def create_embeddings(chunks):
    embeddings = OpenAIEmbeddings(model = "text-embedding-3-small")

    return embeddings.embed_documents(chunks)

# creating vector store 
def build_vector_store(chunks):
    embeddings = OpenAIEmbeddings(model = "text-embedding-3-small")
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local("vector_store")
    return vector_store



