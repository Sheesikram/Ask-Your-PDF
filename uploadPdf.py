from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_groq import ChatGroq


def main():
    load_dotenv()
    os.environ['groq_api_key'] = os.getenv("GROQ_API_KEY")
    groq_api_key = os.getenv("groq_api_key")
    st.set_page_config(page_title="Ask Your PDF", page_icon=":page_with_curl:")
    st.header("Ask Your PDF ")
    # upload file
    pdf = st.file_uploader("Upload a PDF file", type=["pdf"])
    # extract the pdf from the file
    if pdf is not None:
        reader = PdfReader(pdf)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        # st.write(text)
        # as the data is so large we cannot give it to the model at once so we will split the data into chunks
        # split the data into chunks
        # so use langchain for this
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_text(text)
        # st.write(chunks)
        # as you see there are chunks so make it embeddings
        embeddings = HuggingFaceBgeEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )

        # for vectorstore we use facebook ai similarity search FAISS
        Knowledge_base = FAISS.from_texts(chunks, embeddings)
        # show user input
        user_question = st.text_input("Enter Your Question From the PDF", key="name_input")
        
        # Initialize answer as None
        answer = None

        if user_question:
            # get the answer
            answer = Knowledge_base.similarity_search(user_question)
        
        
        if answer:  # Check if answer is not None before proceeding
            # initialize the model
            llm = ChatGroq(
                groq_api_key=groq_api_key,
                model_name="Llama3-8b-8192"
            )
            # load the chain
            chain = load_qa_chain(llm, chain_type="stuff")
            # get the response
            response = chain.run(input_documents=answer, question=user_question)
            st.write(response)
       
    

if __name__ == "__main__":
    main()
