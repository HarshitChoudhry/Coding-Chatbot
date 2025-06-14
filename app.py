import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os


# 1️ Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY not found in environment. Please set it in your .env file.")
    st.stop()


# 2️ Set up LLM and memory if not already in session_state
if "chain" not in st.session_state:
    llm = ChatGroq(
        temperature=0,
        groq_api_key=GROQ_API_KEY,
        model_name="llama3-8b-8192"
    )

    memory = ConversationBufferMemory(memory_key='history', return_messages=True)

    st.session_state.chain = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=False
    )

# 3️ UI: Title
st.title("Your AI Code Assistant - Fast⚡and Context-Aware 🧠")


# 4️ Handle messages + display history

messages = st.session_state.chain.memory.chat_memory.messages
for msg in messages:
    if msg.type == "human":
        st.chat_message("user").code(msg.content)
    else:
        st.chat_message("assistant").markdown(msg.content)


# 5️ Chat input + response generation
if user_input := st.chat_input("Enter your coding problem or question:"):
    # Display user input
    st.chat_message("user").code(user_input)

    # Generate response with context
    response = st.session_state.chain.predict(input=user_input)

    # Display assistant's response
    st.chat_message("assistant").markdown(response)
