import os
from dotenv import load_dotenv
from groq import Groq
import streamlit as st

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY", "").strip(),  # This is the default and can be omitted
)

st.title("Groq Chat and File Analysis Assistant")

user_input = st.text_input("Enter your prompt")
file_input = st.file_uploader("Upload a file", type=["pdf", "docx", "txt","log","json","yaml","yml"])
if file_input:
    file_content = file_input.read()
    print(file_content)
else:
    file_content = "No file needed its an general chat"
    print(file_content)
if st.button("Generate"):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input + f" file content: {file_content}"  ,
            }
        ],
        model="openai/gpt-oss-20b",
        temperature=0.7,
        max_tokens=1000
    )
    st.write(chat_completion.choices[0].message.content)