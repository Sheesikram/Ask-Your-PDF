# Ask Your PDF

**Ask Your PDF** is a Streamlit application that allows users to upload PDF documents and interactively ask questions about the content. It leverages advanced AI models for text embedding, vector storage, and natural language processing to provide accurate and context-aware answers.

---

## Features
- 📄 **Upload and Parse PDFs**: Seamlessly extract and process text from multi-page PDF files.
- 📚 **Chunk-Based Processing**: Efficiently handles large documents by splitting content into manageable chunks.
- 🤖 **AI-Powered Question Answering**: Uses Groq Llama3 for natural language understanding and context-based answers.
- 🔍 **Vector-Based Retrieval**: Utilizes FAISS for similarity search to find relevant document chunks.
- 🚀 **Customizable Embeddings**: Supports HuggingFace embeddings for high-quality text representation.

---
![image](https://github.com/user-attachments/assets/bf277b3d-8ddf-4fb9-9031-229ffbfcf343)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ask-your-pdf.git
   cd ask-your-pdf
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add your API key:
   ```
   GROQ_API_KEY=your_groq_api_key
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py
   ```

---

## Usage
1. **Upload a PDF**: Click the "Upload a PDF file" button and choose your document.
2. **Ask Questions**: Enter your question in the input box, and the AI will provide a relevant answer.
3. **View Results**: See responses directly on the app interface.

---

## Requirements
- Python 3.8+
- Streamlit
- PyPDF2
- LangChain
- FAISS
- HuggingFace Transformers
- Groq API access

---

## File Structure
```
ask-your-pdf/
├── app.py                # Main application file
├── requirements.txt      # Dependencies for the project
├── .env                  # Environment variables (ignored in version control)
├── README.md             # Project description
└── LICENSE               # License file
```

---

## Technologies Used
- **Streamlit**: Interactive web app framework.
- **LangChain**: Text processing and LLM integration.
- **FAISS**: Vector search for efficient document retrieval.
- **HuggingFace Models**: For creating embeddings.
- **PyPDF2**: PDF parsing.

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m "Added a feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## License
This project is licensed under the [MIT License] Shees Ikram(LICENSE).

---

## SEO Keywords
- Ask Your PDF
- Streamlit AI PDF App
- Interactive PDF Question Answering
- LangChain FAISS Application
- HuggingFace Embeddings in Python
- AI PDF Assistant with Groq

---

## Tags
`#Streamlit` `#AI` `#PDF` `#QuestionAnswering` `#FAISS` `#LangChain` `#HuggingFace`
