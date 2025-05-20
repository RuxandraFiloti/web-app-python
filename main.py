import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/girl.jpg") #width=600

with col2:
    st.title("About Me")
    content = """
    Hey! My name is Adda and I am a Full Stack Developer, passionate about Python. This is my portfolio of web apps that I've created so far 😊. Here you can find the built-in apps and their source code. Enjoy!"""
    st.info(content)

description = """Another passion of mine is travelling around the world ✈️🌎. So, this is what I do when I am not coding 😉."""
st.write(description)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5]) #dimensiunea coloanelor

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows(): #sunt afisate primele 10 titluri
        st.header(row["title"]) #key from data.csv
        st.write(row["description"]) # row["description"] - key from data.csv
        st.image("images/" + row["image"]) 
        st.write(f"[Source Code ]({row['url']})") #["Source Code"] - este tag de link pe pagina

with col4:
    for index, row in df[10:].iterrows(): #sunt afisate ultimele 10 titluri
        st.header(row["title"]) #key from data.csv
        st.write(row["description"]) #key from data.csv
        st.image("images/" + row["image"])
        st.write(f"[Source Code ]({row['url']})") 