import os
from typing import Any, List, Dict

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models.openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import Pinecone
import pinecone
from constants import INDEX_NAME

pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENVIRONMENT_REGION"),
)


def run_llm(query: str, chat_history: List[Dict[str, Any]] = []) -> Any:
    embeddings = OpenAIEmbeddings()
    docsearch = Pinecone.from_existing_index(
        index_name=INDEX_NAME, embedding=embeddings
    )
    chat = ChatOpenAI(verbose=True, temperature=0)

    ## Here we need memory to have context from previous prompts
    qa = ConversationalRetrievalChain.from_llm(
        llm=chat, retriever=docsearch.as_retriever(), return_source_documents=True
    )
    return qa({"question": query, "chat_history": chat_history})


def root():
    print(run_llm("What is XIRR?"))
