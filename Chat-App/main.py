import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY", "").strip(),  
)

st.title("Groq Chat Assistant 💬")
user_input = st.text_input("Enter your prompt")
if st.button("Generate"):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="llama-3.1-8b-instant",
    )
    st.write(chat_completion.choices[0].message.content)