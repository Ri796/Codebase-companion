import os
from git import Repo
from dotenv import load_dotenv  
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

def clone_repository(repo_url, local_path):
    """Clones a GitHub repository to a local path."""
    
    if not os.path.exists(local_path):
        print(f"Cloning repository to {local_path}...")
        Repo.clone_from(repo_url, local_path)
    else:
        print("Repository already exists locally.")

def load_documents_from_directory(directory_path)
    """Loads documents from a directory, focusing on common text-based file types
    to improve relevance and speed."""
    
    print("Loading relevant documents from the repository...")
    supported_extensions = [".py", ".md", ".txt", ".json", ".html", ".css", ".js", ".ipynb", "Dockerfile", ".yml", ".yaml"]
    
    documents = []
    for ext in supported_extensions:
        glob_pattern = f"**/*{ext}"
        try:
            loader = DirectoryLoader(
                directory_path, 
                glob=glob_pattern, 
                loader_cls=TextLoader, 
                use_multithreading=True,
                show_progress=False,
                silent_errors=True
            )
            documents.extend(loader.load())
        except Exception as e:
            print(f"Error loading files with extension {ext}: {e}")
            
    print(f"Loaded {len(documents)} documents.")
    return documents

def create_vector_store(documents):
    """Creates a FAISS vector store from a list of documents."""
    if not documents:
        print("No documents were loaded to create a vector store.")
        return None

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)
    
    print("Creating vector store using local embeddings...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    db = FAISS.from_documents(docs, embeddings)
    print("Vector store created successfully.")
    return db

def get_conversational_chain():
    """Creates and returns a conversational question-answering chain."""
    prompt_template = """
    Answer the question as detailed as possible from the provided context...
    """
    
    model = GoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.3)
    chain = load_qa_chain(model, chain_type="stuff")
    return chain
