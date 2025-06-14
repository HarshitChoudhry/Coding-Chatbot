# 🧑‍🏫 Chatbot (Coding Assistant)

This is a **Chatbot designed to help you with coding questions and doubts**.  
It uses **ChatGroq (Groq API)** under the hood to generate clear and helpful code explanations in real time.

---

## 🚀 Features

- **Provides clear and concise code explanations.**
- **Chat-like UI with Streamlit.**
- **Maintains conversation context (Chat Memory) for follow-up questions.**
- **Responsive and lightweight (ChatGroq + Streamlit)**.

---

## 🛠 Tech Stack

- **Python 3.9+**
- **ChatGroq** for Large Language Model.
- **Streamlit** for UI.
- **LangChain** components (`ChatGroq`, `ChatPromptTemplate`) for orchestration.
- **dotenv** for loading environment variables.

---

## ⚙ Installation

1️⃣ **Clone the repository:**

```bash
git clone https://github.com/HarshitChoudhry/Coding-Chatbot.git
cd Chatbot

```

2️⃣ **Create and activate a virtual environment (optional but recommended):**

```bash
python -m venv myenv
myenv\Scripts\activate
```

3️⃣ Install required packages:

```bash
pip install -r requirements.txt
```

## 🔧 Set-up
 Create a .env file in the root directory and add your Groq API key:
```bash
GROQ_API_KEY=your_groq_api_key
```

🚀 **Run the App**

```bash
streamlit run app.py
```


## How It Works
➥ The Streamlit UI lets you enter questions in a chat-like format.
➥ The messages are routed to ChatGroq with a predefined prompt context.
➥ The chatbot maintains Chat Memory to handle follow-up questions accurately.
