from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from utils import get_few_shot_db_chain

st.title("Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)
    st.header("Answer")
    st.write(response)