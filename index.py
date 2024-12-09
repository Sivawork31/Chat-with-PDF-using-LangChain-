# Install necessary libraries

# pip install pypdf                 for extracting text from pdf
# pip install faiss-cpu             for converting words to embeddings(numbers)
# pip install langchain  
# 
# 
# Loading: first we need to load our doc..
# splitting: Break documents into splits of specified size 
# storage: create embeddings and storage the embedding for the splits
# retrival: the app retrieves splits from storage that matched with user query
# Generation: An LLM produces an anser using a promp that include quesiton and respond


#strat with lang chain.document        langchain document already have function to load and read diff type of files
import os
#from langchain.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader



loader = PyPDFLoader("D:\\Projects\\Chat-with-PDF-using-LangChain-\\Finance_Bill.pdf")
page_content = loader.load_and_split()
print(len(page_content),page_content)

text = [doc.page_content for doc in page_content]



from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS


      # enter api key in environment variable  or  inside ()
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(page_content,embeddings)


db.save_local("faiss_index") # for use anytime , so save in local, if we didnt save it in local we need to run from beging and run all also OPenAI embedding have cost , so to avoid paying for that we store it in local

new_db = FAISS.load_local("faiss_index",embeddings)

print(" created and loa successfully")





query = "are there any tax deduction for online gaming"
#docs = new_db.similarity_search(query)
#print(docs)


# Generating answers using llm

from langchain.chains import retrieval_qa
from langchain.chat_models import ChatOpenAI           # chat completion api to answer from doc using openai by rephrasing some words from doc and answer accordingly 
llm = ChatOpenAI()

qa_chain = retrieval_qa.from_chain_type(llm, retriver= new_db.as_retriver())
#res= qa_chain({"query":"are there any tax deduction for online gaming"})

def ask(user_query):
    res= qa_chain({"query": user_query})
    return res["result"]