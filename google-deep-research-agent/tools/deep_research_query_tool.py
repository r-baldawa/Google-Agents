#!/usr/bin/env python3
"""
Deep Research Query Tool for watsonx Orchestrate

This tool provides access to Google's Deep Research capabilities through
a simple interface that accepts a research question from the UI.
Uses OAuth 2.0 credentials from watsonx Orchestrate Connections.
"""

import os
import json
import requests
from typing import Optional

# Conditional import for tool decorator (only needed during import, not runtime)
try:
    from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission
except ImportError:
    # When running in watsonx Orchestrate server, the decorator is not needed
    def tool(permission=None, expected_credentials=None):
        """Dummy decorator for runtime execution"""
        def decorator(func):
            return func
        return decorator
    
    class ToolPermission:
        READ_ONLY = "read_only"

# Deep Research Configuration
LOCATION = "global"
AGENT_MODEL = "deep-research-pro-preview-12-2025"
API_ENDPOINT = "https://aiplatform.googleapis.com"


def parse_streaming_event(response_line: str) -> Optional[dict]:
    """Parse a streaming event line from the API response."""
    if not response_line.startswith("data: "):
        return None
    json_str = response_line[len("data: "):].strip()
    if json_str == "[DONE]":
        return None
    
    try:
        return json.loads(json_str)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None


@tool(
    permission=ToolPermission.READ_ONLY,
    expected_credentials=[
        {"app_id": "vertex_oauth_code", "type": "oauth2_auth_code"}
    ]
)
def deep_research_query(question: str, credentials: dict = None) -> dict:
    """
    Execute comprehensive research on any topic using Google's Deep Research agent.
    
    This tool performs in-depth analysis by:
    - Searching multiple authoritative sources
    - Analyzing and synthesizing information
    - Providing detailed insights with citations
    - Including source references
    
    Use this tool when you need thorough research on complex topics, competitive
    analysis, market research, or detailed information gathering.
    
    Args:
        question: The research question or topic to investigate in detail
        credentials: OAuth 2.0 credentials from vertex_oauth_code connection (auto-injected)
    
    Returns:
        dict: Research results including:
            - success: Boolean indicating if the request was successful
            - interaction_id: Unique ID for this research interaction
            - question: The original research question
            - summary: A concise summary of findings
            - full_response: Complete detailed research response
            - status: Status of the research (completed/failed)
    
    Example:
        result = deep_research_query("What are the latest trends in AI for 2025?")
    """
    # Get credentials from connection or fallback to environment
    auth_token = None
    project_id = os.getenv("GOOGLE_PROJECT_ID", "883982946869")
    
    if credentials:
        # Try different possible credential formats
        if isinstance(credentials, dict):
            # Try access_token (OAuth standard)
            auth_token = credentials.get("access_token")
            # Try token (alternative format)
            if not auth_token:
                auth_token = credentials.get("token")
            # Try bearer_token (another alternative)
            if not auth_token:
                auth_token = credentials.get("bearer_token")
            # Get project_id if provided
            project_id = credentials.get("project_id", project_id)
    
    # Fallback to environment variables for local testing
    if not auth_token:
        auth_token = os.getenv("GOOGLE_AUTH_TOKEN")
    
    if not auth_token:
        return {
            "success": False,
            "error": "Authentication token not found. Please configure vertex_oauth_code connection in watsonx Orchestrate.",
            "question": question,
            "debug_info": {
                "credentials_received": credentials is not None,
                "credentials_type": type(credentials).__name__ if credentials else None,
                "credentials_keys": list(credentials.keys()) if isinstance(credentials, dict) else None
            }
        }
    
    # Build API request
    base_url = f"{API_ENDPOINT}/v1beta1/projects/{project_id}/locations/{LOCATION}/interactions"
    
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "stream": True,
        "background": True,
        "agent": AGENT_MODEL,
        "input": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": question
                    }
                ]
            }
        ],
        "tools": [
            {
                "type": "google_search"
            }
        ]
    }
    
    # Execute request
    interaction_id = None
    response_lines = []
    text_content = []
    
    try:
        response = requests.post(
            base_url,
            headers=headers,
            json=payload,
            stream=True,
            timeout=120
        )
        
        if response.status_code == 200:
            # Process streaming response
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    response_lines.append(decoded_line)
                    
                    # Parse for interaction ID and content
                    event_data = parse_streaming_event(decoded_line)
                    if event_data:
                        # Extract interaction ID
                        if "interaction" in event_data and "id" in event_data["interaction"]:
                            interaction_id = event_data["interaction"]["id"]
                        
                        # Extract text content from deltas
                        if "delta" in event_data and "text" in event_data.get("delta", {}):
                            text_content.append(event_data["delta"]["text"])
            
            # Combine all text content
            full_text = "".join(text_content)
            
            # Create a summary (first 500 characters)
            summary = full_text[:500] + "..." if len(full_text) > 500 else full_text
            
            return {
                "success": True,
                "interaction_id": interaction_id,
                "question": question,
                "summary": summary,
                "full_response": full_text,
                "status": "completed"
            }
        else:
            return {
                "success": False,
                "error": f"API returned status {response.status_code}",
                "details": response.text,
                "question": question
            }
            
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "Request timed out after 120 seconds",
            "question": question,
            "note": "The research may still be processing in the background"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "question": question
        }


if __name__ == "__main__":
    # Test the tool
    from dotenv import load_dotenv
    load_dotenv()
    
    print("Testing Deep Research Query Tool...")
    test_question = "What is the weather in Toronto, Canada?"
    result = deep_research_query(test_question)
    
    # Handle ToolResponse object
    if hasattr(result, 'content'):
        print(json.dumps(result.content, indent=2))
    else:
        print(json.dumps(result, indent=2))

# Made with Bob
