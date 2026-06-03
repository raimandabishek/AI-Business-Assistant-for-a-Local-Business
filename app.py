import streamlit as st

from scraper import get_website_content
from analyzer import analyze_business

st.title("AI Business Assistant")

website_url = st.text_input("Business Website URL")

reviews = st.text_area("Business Google Reviews")

competitor_reviews = st.text_area("Competitor Google Reviews")

competitor_url = st.text_input("Competitor Website URL")


if st.button("Analyze"):

    with st.spinner("Analyzing..."):

        website_content = get_website_content(website_url)

        result = analyze_business(
            website_content,
            reviews,
            competitor_url
        )

        st.subheader("Business Analysis Report")

        st.markdown(result)