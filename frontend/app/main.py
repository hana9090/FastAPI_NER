# frontend/main.py

import requests
import streamlit as st
from processing import process
# defines an h1 header
st.title("NER with Spacy & FastAPI")

st.header("Check if FastAPI is live:")
hello = requests.get('http://host.docker.internal:8080/').json()
st.write(hello)


st.header("Named Entity Recognition")
# input field for text
text_input = st.text_area("Enter the text")
text_dict = {"text": text_input}


# Click button to send string to fast a button
if st.button("Start NER"):
        # Send POST request to FastAPI
        entities = process(text_dict)
        # Print response as JSON
        st.json(entities)

