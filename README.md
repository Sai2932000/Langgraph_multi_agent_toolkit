# 🌐 LangGraph React Agent with Tools 

This project demonstrates how to build a **LangGraph-powered React Agent** with multiple integrated tools, 
a memory checkpoint system, LangSmith tracing, and added Langgraph Client Sdk for accessing agent from outside the process where it was defined.

## 🚀 Features

- **ReAct Agent with LangGraph** – Structured agent execution using `StateGraph`.
- **Tools Integrated:**
  - 🔍 Tavily Search (Finance search with images)
  - 📲 Twilio SMS Sender
  - 🎥 YouTube Search
  - 📚 Wikipedia Search
- **Memory with InMemorySaver** – Keeps track of conversations.
- **LangSmith Tracing** – Monitor and debug agent runs.
- 📡 **LangGraph Client SDK** – Access the graph outside its process.


## 📦 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/Sai2932000/Langgraph_multi_agent_toolkit.git
cd your-repo
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the root folder and set the following keys:

```env
# Google Vertex AI
GOOGLE_APPLICATION_CREDENTIALS=your_service_account.json

# Twilio API
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+1234567890

# LangSmith (for tracing)
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=your_project_name
```

## ▶️ Usage

**Run the Graph:**

```bash
langgraph dev --allow-blocking --port 3000
```
**Run SDK**

```bash
python client.py
```

## 📂 Project Structure

```
.
├── main.py              # Core LangGraph ReAct agent with tools
├── client.py            # Accessing Graph remotely
├── requirements.txt     # Dependencies
├── .env.example         # Example environment file
└── README.md            # Documentation
```

## ⚡ Example Queries

- "Search finance news about stock markets"
- "Send SMS to +1234567890 saying Hello from LangGraph!"
- "Search YouTube videos about Lex Fridman"
- "Who was Bahubali?"

## 🛠️ Tech Stack

- **LangGraph** – Agent orchestration
- **LangChain** – Tooling ecosystem
- **Google Vertex AI (Gemini)** – LLM backbone
- **Twilio** – SMS messaging
- **Tavily** – Search engine
- **Wikipedia & YouTube APIs**
- **Client** - Accessing Graph remotely
- **LangSmith** – Tracing & observability


-**📊 Architecture**

User (Client SDK)
        │
        ▼
  LangGraph Server (ReAct Agent)
        │
  ┌───────────────┬───────────────┬───────────────┐
  ▼               ▼               ▼               ▼
Tavily       Twilio SMS       YouTube API     Wikipedia


---

### 💡 Notes
- Make sure your Google Cloud credentials are set correctly for VertexAI.
- Tracing can be viewed in [LangSmith](https://smith.langchain.com/).
- Extend tools by adding more from `langchain_community`.