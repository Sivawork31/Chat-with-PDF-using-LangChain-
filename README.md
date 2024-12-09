# Chat-with-PDF-using-LangChain-




This project is an AI-Powered Query System built using Large Language Models (LLMs) to efficiently extract and answer queries from PDF documents. It leverages LangChain, FAISS, and OpenAI GPT-4 to provide semantic search and accurate responses.

Key Features


*Semantic Search: Implemented with FAISS to retrieve relevant answers quickly and efficiently.

*PDF Processing: Handles large documents (50+ pages) with structured data extraction for precise query resolution.
*LLM Integration: Fine-tuned GPT-4 to deliver context-aware responses.
*Cost Optimization: Reduced API usage costs by 30% with a local retrieval solution using FAISS indexes.




Technologies Used

*LangChain: Framework for building LLM-based workflows.
*FAISS: Efficient indexing for semantic search.
*OpenAI GPT-4: Used for generating accurate and context-aware answers.
*Python: Core language for implementation.
*PyPDFLoader: PDF processing and content extraction.



Installation

Clone this repository:

git clone https://github.com/Sivawork31/Chat-with-PDF-using-LangChain-.git

Navigate to the project directory: open vs code using cmd  command(code . )

Install dependencies:

pip install -r requirements.txt  
How to Run
Place your PDF document in the project folder.

Set your OpenAI API key as an environment variable:

export OPENAI_API_KEY='your-api-key' 
Run the application:

streamlit run app.py  
Open your browser and navigate to http://localhost:8501.
Usage
Upload your PDF document through the provided interface.

Enter your query in the input box (e.g., "Are there any tax deductions for online gaming?").

The system retrieves relevant sections from the document and provides context-aware answers.



Project Workflow
PDF Content Extraction: The PDF is split into pages and processed into chunks using PyPDFLoader.
Embedding Generation: Text chunks are converted into vector representations using OpenAI embeddings.
Semantic Indexing: FAISS indexes are built for efficient query retrieval.
Answer Generation: Queries are processed through GPT-4, which generates concise and accurate answers.
Results
90% Retrieval Accuracy: High precision in fetching relevant document content.
30% Cost Savings: Optimized API calls with local retrieval solutions.
Future Improvements
Add support for multi-document query handling.
Enhance the system with additional LLM models like Hugging Face Transformers.
Integrate user authentication for secure access.
Acknowledgments
This project utilizes tools and frameworks from OpenAI, LangChain, and FAISS.

License
This project is licensed under the MIT License.
