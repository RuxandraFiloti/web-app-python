import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/girl.jpg") #width=600

with col2:
    st.title("About Me")
    content = """
    Hey! My name is Adda and I am a Full Stack Developer, passionate about Python. This is my portfolio of web apps that I've created so far 😊. Here you can find the built-in apps and their source code. Enjoy!"""
    st.info(content)