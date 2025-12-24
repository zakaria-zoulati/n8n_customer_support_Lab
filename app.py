import streamlit as st
import requests

st.title("AI Customer Support")

msg = st.text_input("How can we help you?")

if st.button("Send"):
    res = requests.post("http://localhost:5678/webhook/customer", json={"message": msg})
    st.write(res.json())
