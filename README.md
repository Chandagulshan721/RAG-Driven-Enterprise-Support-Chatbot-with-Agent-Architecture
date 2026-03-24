# 🤖 Agentic AI RAG Chatbot Project

A complete **Agentic AI + RAG (Retrieval-Augmented Generation) Chatbot** built using **Python, Flask, and LLM tools**.
This project demonstrates how an AI agent can **retrieve company knowledge, use tools, make decisions, and respond intelligently through a web interface**.

---

# 🚀 Project Overview

This project simulates a **real-world AI assistant** that can:

* Answer company policy questions using RAG
* Perform calculations using a calculator tool
* Check order status using a tool
* Maintain conversation memory
* Store chat history in database
* Upload company documents dynamically
* Respond through a ChatGPT-like web interface

---

# 🧠 Agentic AI Flow

User → Web Interface → Flask App → Agent Service → Tools / RAG → LLM → Response → UI

---

# 🏗️ Project Architecture

```
User Interface (index.html)
        ↓
Flask App (app.py)
        ↓
Agent Service (agent_service.py)
        ↓
Decision Engine
   ↙        ↓        ↘
RAG     Calculator    Order Tool
(rag_service.py)  (tools.py)
        ↓
Company Documents
(data/company_docs.txt)
        ↓
LLM Response
```

---

# 📂 Project Structure

```
agentic-ai-rag-project

app.py
agent_service.py
rag_service.py
tools.py
database.py
test_agent.py
test_rag.py

requirements.txt
README.md
.gitignore

templates/
    index.html

data/
    company_docs.txt
```

---

# 🖼️ Chatbot Output

### ChatGPT Style Interface


<img width="753" height="730" alt="Screenshot 2026-03-24 213752" src="https://github.com/user-attachments/assets/cc74118b-ccae-4da3-b6fb-41275884b6e6" />


---

# ⚙️ Tech Stack

* Python 3.10
* Flask
* Groq API (LLM)
* RAG (Retrieval-Augmented Generation)
* LangChain
* HTML / CSS / JavaScript
* SQLite Database
* Agentic AI Decision Logic

---

# 🧰 Tools Used

* Calculator Tool
* Order Status Tool
* Policy Retrieval Tool
* Conversation Memory
* Document Upload

---

# 📌 Features

✔ RAG-based knowledge retrieval
✔ Agent decision-making system
✔ Multi-tool integration
✔ ChatGPT-style UI
✔ Chat history storage
✔ File upload for company documents
✔ Secure API key using .env
✔ Flask web application

---

# 🔐 Security

* API keys stored in `.env`
* `.gitignore` used
* Database protected
* No secrets exposed

---

# ▶️ How to Run the Project

## Step 1

Clone the repository

```
git clone https://github.com/yourusername/agentic-ai-rag-project.git
```

---

## Step 2

Go to project folder

```
cd agentic-ai-rag-project
```

---

## Step 3

Install dependencies

```
pip install -r requirements.txt
```

---

## Step 4

Create `.env` file

```
GROQ_API_KEY=your_api_key_here
```

---

## Step 5

Run the app

```
python app.py
```

---

## Step 6

Open browser

```
http://127.0.0.1:5000
```

---

# 🧪 Test the Agent

Try questions like:

```
What is return policy?
2 + 5
Check my order
Tell me about exchange policy
```

---

# 📌 Future Improvements

* Docker deployment
* Multi-user login
* Vector database (FAISS)
* Real-time API integration
* Cloud deployment
* Advanced agent orchestration

---

# 🎯 Learning Outcome

This project helps understand:

* Agentic AI
* RAG pipeline
* Tool-based AI systems
* LLM integration
* Flask backend
* Real-world AI architecture

---

# 👨‍💻 Author

CHANDA GULSHAN 

AI Engineer | Python Developer | Agentic AI Enthusiast

---

# ⭐ If you like this project

Give it a star on GitHub
