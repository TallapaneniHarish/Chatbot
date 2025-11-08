import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq 

load_dotenv()

st.set_page_config(
    page_title="Chat with Groq Llama3!",
    page_icon=":brain:",
    layout="centered",
)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


st.title("🤖 Groq - ChatBot")


for message in st.session_state.chat_history:
    if message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(message["content"])
    else:
        with st.chat_message("user"):
            st.markdown(message["content"])


user_prompt = st.chat_input("Ask Groq Llama3...")


if user_prompt:

    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})


    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=st.session_state.chat_history
    )


    model_reply = completion.choices[0].message.content


    st.chat_message("assistant").markdown(model_reply)


    st.session_state.chat_history.append({"role": "assistant", "content": model_reply})
