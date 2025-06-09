** RAG Agent - Federal Documents Chatbot
**

This project implements a **Retrieval-Augmented Generation (RAG) Agent** that allows users to interact with U.S. federal government documents (like executive orders, memoranda, etc.) through a natural language interface.

Users can ask questions like:
- _"Show documents signed by Trump between May 20 and May 25, 2025"_
- _"Summarize all executive orders from the past 10 days"_
- _"Were any memorandums published recently?"_

In addition to querying federal documents, the chatbot can also answer general questions and casual queries, such as:

- _"What is Newton’s 3rd law?"_
- _"Tell me a joke"_
- 
## 📁 Project Structure

rag_agent_project/
├── agent/ # RAG agent logic (prompts, tools, routing)
├── api/ # FastAPI backend
├── db/ # Database connector
├── pipeline/ # ETL pipeline (fetch, clean, load federal data)
├── ui/ # Simple HTML frontend
├── venv/ # Python virtual environment (excluded from Git)
├── .gitignore
├── README.md
├── requirements.txt


# Features

-  Query executive documents using natural language
-  RAG pipeline with custom tools
-  MySQL backend integration
-  Frontend with HTML + Tailwind CSS
-  FastAPI-based chat interface

##  Setup

 1. Clone the repository

git clone https://github.com/ApurvaPatil2401/rag-agent.git
cd rag-agent

2. Create & activate virtual environment

python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Configure MySQL
Make sure you have a MySQL server running. Create a database named federal_data, and create a table named federal_documents as per your pipeline logic.

5. Run the pipeline

cd pipeline
python loader.py

6. Start the backend API

cd api
uvicorn server:app --reload

7. Open the frontend

Open ui/index.html in a browser. Start chatting!

📦 Example Queries
Show documents signed by Trump in April 2025
Summarize executive orders from the last 2 weeks
Did any memorandums get published last week?

📜 License
This project is for educational/demo purposes. 


