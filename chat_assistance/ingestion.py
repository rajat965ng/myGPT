import os
from langchain.document_loaders import ReadTheDocsLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import pinecone
from constants import INDEX_NAME

pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENVIRONMENT_REGION"),
)


def load_docs():
    loader = ReadTheDocsLoader(
        path="langchain-docs", custom_html_tag=("html", {})
    )
    raw_data = loader.load()
    print(raw_data)
    print(f"The length of docs array is {len(raw_data)}")
    splitter = RecursiveCharacterTextSplitter(
        chunk_overlap=100, chunk_size=1000, separators=["\n\n", "\n", " ", ""]
    )
    documents = splitter.split_documents(documents=raw_data)
    print(f"splitted in to documents size {len(documents)}")

    for doc in documents:
        old_path = doc.metadata["source"]
        new_url = old_path.replace("langchain-docs/", "https://")
        doc.metadata.update({"source": new_url})

    print(f"Documents with updates {documents}")

    embeddings = OpenAIEmbeddings()
    Pinecone.from_documents(
        documents=documents, embedding=embeddings, index_name=INDEX_NAME
    )
    print("*** Added to vector store ***")


def root():
    load_docs()
