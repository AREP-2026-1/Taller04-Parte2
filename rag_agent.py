from langchain_anthropic import ChatAnthropic
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter

DOCS = [
    "AREP course: This project demonstrates LangChain agents and tools.",
    "RAG combines retrieval with generation to ground answers in context.",
    "Use vector embeddings to index documents for similarity search.",
    "LangChain provides chains, retrievers, and integrations for RAG.",
]

def build_retriever():
    splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
    chunks = splitter.create_documents(DOCS)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore.as_retriever(search_kwargs={"k": 3})

def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)

def build_chain():
    llm = ChatAnthropic(
        model="claude-sonnet-4-5-20250929",
        temperature=0,
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Answer the user using the provided context. If unsure, say you don't know."),
            ("human", "Question: {input}\n\nContext:\n{context}"),
        ]
    )

    retriever = build_retriever()
    chain = (
        {
            "context": retriever | RunnableLambda(format_docs),
            "input": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain

if __name__ == "__main__":
    chain = build_chain()
    result = chain.invoke("What is RAG and why is it useful?")
    print(result)