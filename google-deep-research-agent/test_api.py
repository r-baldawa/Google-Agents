#!/usr/bin/env python3
"""
Google Deep Research Agent - API Test Script

This script tests the Google Deep Research API connection with a simple query.
Use this to verify your Google Cloud credentials are working correctly.
"""

import os
import sys
import json
import time
from dotenv import load_dotenv
import requests

# Colors for terminal output
class Colors:
    GREEN = '\033[0;32m'
    RED = '\033[0;31m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;36m'
    NC = '\033[0m'  # No Color

def print_header(text):
    """Print a formatted header"""
    print(f"\n{Colors.BLUE}{'='*70}")
    print(f"{text}")
    print(f"{'='*70}{Colors.NC}\n")

def print_success(text):
    """Print success message"""
    print(f"{Colors.GREEN}✅ {text}{Colors.NC}")

def print_error(text):
    """Print error message"""
    print(f"{Colors.RED}❌ {text}{Colors.NC}")

def print_info(text):
    """Print info message"""
    print(f"{Colors.BLUE}ℹ️  {text}{Colors.NC}")

def test_deep_research_api():
    """Test the Google Deep Research API"""
    print_header("🧪 Testing Google Deep Research API")
    
    # Load environment variables
    load_dotenv()
    auth_token = os.getenv('GOOGLE_AUTH_TOKEN')
    project_id = os.getenv('GOOGLE_PROJECT_ID')
    
    if not auth_token or auth_token == 'your_google_auth_token_here':
        print_error("Google Auth Token not set in .env")
        print("\nGet token with: gcloud auth print-access-token")
        return False
    
    if not project_id or project_id == 'your_project_id_here':
        print_error("Google Project ID not set in .env")
        return False
    
    print_info(f"Project ID: {project_id}")
    print_info(f"Token length: {len(auth_token)} characters")
    
    # Test query
    test_query = "What are the latest developments in quantum computing?"
    print_info(f"Test query: {test_query}")
    
    try:
        # Step 1: Create interaction
        print("\n📝 Step 1: Creating interaction...")
        url = f"https://aiplatform.googleapis.com/v1beta1/projects/{project_id}/locations/global/interactions"
        headers = {
            "Authorization": f"Bearer {auth_token}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "query": test_query,
            "response_modalities": ["TEXT"]
        }
        
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        
        if response.status_code != 200:
            print_error(f"Failed to create interaction (Status: {response.status_code})")
            print(f"Response: {response.text}")
            
            if response.status_code == 401:
                print("\n⚠️  Token expired or invalid")
                print("Get fresh token with: gcloud auth print-access-token")
            elif response.status_code == 403:
                print("\n⚠️  Permission denied")
                print("Make sure Deep Research API is enabled for your project")
            
            return False
        
        result = response.json()
        interaction_name = result.get('name')
        print_success(f"Interaction created: {interaction_name}")
        
        # Step 2: Poll for results
        print("\n⏳ Step 2: Waiting for research results...")
        print("(This may take 30-60 seconds...)")
        
        max_attempts = 60
        attempt = 0
        
        while attempt < max_attempts:
            time.sleep(2)
            attempt += 1
            
            # Get interaction status
            get_url = f"https://aiplatform.googleapis.com/v1beta1/{interaction_name}"
            get_response = requests.get(get_url, headers=headers, timeout=10)
            
            if get_response.status_code != 200:
                print_error(f"Failed to get interaction status (Status: {get_response.status_code})")
                return False
            
            interaction_data = get_response.json()
            state = interaction_data.get('state', 'UNKNOWN')
            
            if state == 'COMPLETED':
                print_success("Research completed!")
                
                # Extract and display results
                print("\n" + "="*70)
                print("📊 RESEARCH RESULTS")
                print("="*70 + "\n")
                
                # Get the response
                response_text = interaction_data.get('response', {}).get('text', 'No response text')
                print(f"{response_text}\n")
                
                # Get citations
                citations = interaction_data.get('response', {}).get('citations', [])
                if citations:
                    print("\n📚 CITATIONS:")
                    for i, citation in enumerate(citations, 1):
                        title = citation.get('title', 'No title')
                        url = citation.get('url', 'No URL')
                        print(f"{i}. {title}")
                        print(f"   {url}\n")
                else:
                    print("No citations provided")
                
                return True
            
            elif state == 'FAILED':
                print_error("Research failed")
                error = interaction_data.get('error', {})
                print(f"Error: {error}")
                return False
            
            # Still processing
            if attempt % 5 == 0:
                print(f"   Still processing... ({attempt * 2}s elapsed)")
        
        print_error("Timeout waiting for results")
        return False
        
    except requests.exceptions.Timeout:
        print_error("Request timed out")
        return False
    except requests.exceptions.RequestException as e:
        print_error(f"Request failed: {e}")
        return False
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        return False

def main():
    """Main function"""
    print_header("🔬 Google Deep Research API Test")
    
    success = test_deep_research_api()
    
    print_header("📊 Test Summary")
    
    if success:
        print_success("API test passed!")
        print("\nYour Google Cloud credentials are working correctly.")
        print("You can now deploy the agent with: ./deploy.sh")
        sys.exit(0)
    else:
        print_error("API test failed")
        print("\nPlease check:")
        print("1. Your Google Auth Token is valid (not expired)")
        print("2. Deep Research API is enabled for your project")
        print("3. Your project ID is correct")
        print("\nSee AUTHENTICATION_SETUP.md for help")
        sys.exit(1)

if __name__ == "__main__":
    main()

# Made with Bob
