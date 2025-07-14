import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = api_key

# Streamlit UI
st.set_page_config(page_title="Finance Q&A", layout="wide")
st.title("📰 Finance Research Q&A App")
st.markdown("Ask questions about finance articles scraped from the web.")

urls = st.text_area("Paste finance article URLs (one per line)", height=150).splitlines()
question = st.text_input("Ask a question based on the articles")

if st.button("Run QA") and urls and question:
    with st.spinner("🔄 Loading documents and preparing answer..."):
        try:
            # Load docs
            loader = WebBaseLoader(urls)
            docs = loader.load()

            # Split
            splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
            chunks = splitter.split_documents(docs)

            # Embeddings & VectorStore
            embeddings = OpenAIEmbeddings()
            vector_store = FAISS.from_documents(chunks, embeddings)

            # Retrieval Chain
            llm = OpenAI(temperature=0.7)
            qa_chain = RetrievalQAWithSourcesChain.from_llm(llm, retriever=vector_store.as_retriever())

            # Ask question
            result = qa_chain.invoke({"question": question})
            st.subheader("Answer:")
            st.write(result.get("answer", "No answer found."))

            st.subheader("Sources:")
            st.write(result.get("sources", "No sources found."))
        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")
