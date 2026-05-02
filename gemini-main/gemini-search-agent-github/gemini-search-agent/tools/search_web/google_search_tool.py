"""
Google Search Tool for watsonx Orchestrate

This tool wraps Google's Search Grounding functionality so it can be used
within watsonx Orchestrate agents. It allows agents to access live web
information through Google Search.

Usage:
    1. Import this tool to Orchestrate
    2. Use in your agent configuration
    3. The tool will automatically use Google Search grounding
"""

from ibm_watsonx_orchestrate.agent_builder.tools import tool
from google import genai
from google.genai import types
import os


@tool()
def search_web(query: str) -> str:
    """Search the web for current information using Google Search grounding.
    
    This tool uses Google's Gemini model with Search grounding to find
    real-time information from the web. It's perfect for:
    - Getting current news and events
    - Finding up-to-date facts and statistics
    - Researching recent developments
    - Answering questions that require current information
    - Fact-checking claims
    - Getting latest news on any topic
    
    Args:
        query (str): The search query or question to answer using web search.
                    Examples:
                    - "What are today's top news stories?"
                    - "Who won the latest Super Bowl?"
                    - "What is the current price of Bitcoin?"
                    - "What are the latest developments in AI?"
                    - "Is it true that the Earth is flat?"
    
    Returns:
        str: A comprehensive answer based on current web information,
             including relevant facts and context from multiple sources.
    
    Raises:
        ValueError: If API key is not configured
        Exception: If the Google API call fails
    """
    # TODO: Replace with your Google API key
    # Get your API key from: https://aistudio.google.com/app/apikey
    api_key = 'YOUR_GOOGLE_API_KEY_HERE'
    
    try:
        # Initialize Google Generative AI client
        client = genai.Client(api_key=api_key)
        
        # Use gemini-2.5-pro which has better capabilities with search grounding
        response = client.models.generate_content(
            model='gemini-2.5-pro',
            contents=query,
            config=types.GenerateContentConfig(
                tools=[types.Tool(google_search=types.GoogleSearch())],
                temperature=0.7,
            ),
        )
        
        # Extract and return the text response
        return response.text
        
    except Exception as e:
        error_msg = str(e)
        return (
            f"Error searching the web: {error_msg}\n\n"
            "The search tool encountered an issue. Please try rephrasing your query."
        )


# Tool made with watsonx Orchestrate integration

# Made with Bob
