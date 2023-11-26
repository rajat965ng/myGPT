import streamlit.web.bootstrap as bootstrap


def root():
    bootstrap.run("chat_assistance/gpt.py", "streamlit", "run", {})
