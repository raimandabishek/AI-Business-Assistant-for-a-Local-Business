# AI Business Assistant for Local Businesses

## Overview

An AI-powered assistant that analyzes a business using:

* Business Website URL
* Customer Reviews
* Competitor Website URL

The system identifies business problems, opportunities, competitor advantages, and generates actionable recommendations.

## Features

* Website Content Analysis
* Customer Review Analysis
* Competitor Analysis
* AI-Powered Business Insights
* Prioritized Action Plan

## Technology Stack

* Python
* Streamlit
* BeautifulSoup
* Requests
* Groq API
* Llama 3.3 70B

## Architecture

User Input
↓
Streamlit UI
↓
Website Scraper
↓
Prompt Builder
↓
Groq Llama 3.3
↓
Business Analysis Report

## Project Structure

business-ai-assistant/

├── app.py

├── scraper.py

├── analyzer.py

├── requirements.txt

├── README.md

## Run Application

Install dependencies:

pip install -r requirements.txt

Run:

streamlit run app.py
