import streamlit as st
import shutil
import os
import stat
from utils import clone_repository, load_documents_from_directory, create_vector_store, get_conversational_chain

# function to delete the temp directory on Windows 
def remove_readonly(func, path, excinfo):
    """
    Error handler for shutil.rmtree.

    If the error is due to an access error (read-only file),
    it attempts to add write permission and then retries the removal.
    """
    if not os.access(path, os.W_OK):
        # Is the error an access error?
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise

def user_input(user_question, db):
    """Handles user input and displays the chatbot's response."""
    chain = get_conversational_chain()
    docs = db.similarity_search(user_question)
    
    response = chain(
        {"input_documents": docs, "question": user_question},
        return_only_outputs=True
    )
    
    st.write("Reply: ", response["output_text"])

def main():
    st.set_page_config("Codebase Companion")
    st.header("Chat with your GitHub Repository 🤖")

    repo_url = st.text_input("Enter the GitHub Repository URL:")

    if "vector_store" not in st.session_state:
        st.session_state.vector_store = None

    if st.button("Process Repository"):
        if repo_url:
            with st.spinner("Processing... This may take a few minutes for large repositories."):
                local_path = "temp_repo"

                # deletion method 
                if os.path.exists(local_path):
                    # Pass the special error handler to shutil.rmtree
                    shutil.rmtree(local_path, onerror=remove_readonly)
                
                # Clone the repository
                clone_repository(repo_url, local_path)
                
                # Load the documents
                documents = load_documents_from_directory(local_path)
                
                # Create the vector store
                if documents:
                    st.session_state.vector_store = create_vector_store(documents)
                    st.success("Repository processed successfully! You can now ask questions.")
                else:
                    st.warning("Could not find any relevant documents in the repository. Please try a different one.")
                    st.session_state.vector_store = None # Reset in case of failure
        else:
            st.warning("Please enter a GitHub repository URL.")

    # Only show the question input if the repository has been processed
    if st.session_state.vector_store:
        user_question = st.text_input("Ask a Question about the Codebase:")
        if user_question:
            user_input(user_question, st.session_state.vector_store)

if __name__ == "__main__":
    main()
