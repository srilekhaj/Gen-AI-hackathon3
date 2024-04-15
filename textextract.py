# extract text
from langchain.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_google_genai import GoogleGenerativeAIEmbeddings


llm = ChatGoogleGenerativeAI(
        google_api_key="AIzaSyBuBnDizsZfq0tai2ExloP8TvTuYCV8_ss",
        model="gemini-pro",
        convert_system_message_to_human=True
        
    )


embeddings = GoogleGenerativeAIEmbeddings(
    google_api_key="AIzaSyBuBnDizsZfq0tai2ExloP8TvTuYCV8_ss",
    model="models/embedding-001",


)

persist_directory = "C:/Users/DELL/OneDrive/GenAI-usecase/dbdum1/"

# Set the embedding function and directory for vector storage
embedding = embeddings
vectordb = Chroma(embedding_function=embedding, persist_directory=persist_directory)

def text_retriever(Query):
        # Set up retriever for retrieving relevant information
    retriever = vectordb.similarity_search(Query, k=1)

    for ele in retriever:
        content = ele.page_content
    return content