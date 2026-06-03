import streamlit as st

st.title("AI Business Assistant")

website_url = st.text_input("Business Website URL")

reviews = st.text_area("Paste Google Reviews")

competitor_url = st.text_input("Competitor Website URL")

if st.button("Analyze"):
    st.success("Data Received!")
    
    st.write("Website:", website_url)
    st.write("Competitor:", competitor_url)
    st.write("Reviews:", reviews)