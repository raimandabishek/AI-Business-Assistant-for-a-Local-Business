from groq import Groq

client = Groq(
    api_key="YOUR_GROQ_API_KEY"
)

def analyze_business(website_content, reviews, competitor_url):

    prompt = f"""
    Analyze this business.

    Website Content:
    {website_content}

    Reviews:
    {reviews}

    Competitor Website:
    {competitor_url}

    Provide:

    1. Business Analysis Summary
    2. Key Findings
    3. Competitor Insights
    4. Recommendations
    5. Prioritized Action Plan

    Give practical business recommendations.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content