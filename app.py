import os
from dotenv import load_dotenv
from groq import Groq
import streamlit as st

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY", "").strip(),  # This is the default and can be omitted
)

st.title("Groq Chat")

user_input = st.text_input("Enter your prompt")
if st.button("Generate"):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="openai/gpt-oss-20b",
    )
    st.write(chat_completion.choices[0].message.content)