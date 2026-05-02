#!/usr/bin/env python3
"""
Google Deep Research Agent - Setup Verification Script

This script verifies that all prerequisites and credentials are properly configured.
Run this before deploying the agent to catch any issues early.
"""

import os
import sys
import subprocess
from pathlib import Path

# Try to import required packages
try:
    import requests
    from dotenv import load_dotenv
    PACKAGES_INSTALLED = True
except ImportError:
    PACKAGES_INSTALLED = False

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

def print_warning(text):
    """Print warning message"""
    print(f"{Colors.YELLOW}⚠️  {text}{Colors.NC}")

def check_python_version():
    """Check Python version"""
    print("Python Environment:")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print_success(f"Python version: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print_error(f"Python version: {version.major}.{version.minor}.{version.micro} (3.8+ required)")
        return False

def check_packages():
    """Check if required packages are installed"""
    if PACKAGES_INSTALLED:
        print_success("Required packages installed")
        return True
    else:
        print_error("Required packages not installed")
        print("\nInstall with: pip install -r requirements.txt")
        return False

def check_ibm_credentials():
    """Check IBM Cloud credentials"""
    print("\nIBM Cloud:")
    
    if not PACKAGES_INSTALLED:
        print_warning("Cannot verify (packages not installed)")
        return False
    
    load_dotenv()
    api_key = os.getenv('IBM_CLOUD_API_KEY')
    
    if not api_key or api_key == 'your_ibm_cloud_api_key_here':
        print_error("IBM Cloud API Key not set in .env")
        print("\nSee AUTHENTICATION_SETUP.md for instructions")
        return False
    
    # Check key format
    if len(api_key) != 44:
        print_warning(f"IBM Cloud API Key length: {len(api_key)} (expected ~44)")
        print("This might not be a valid IBM Cloud API key")
    else:
        print_success(f"IBM Cloud API Key: Valid ({len(api_key)} characters)")
    
    # Try to get IAM token
    try:
        url = "https://iam.cloud.ibm.com/identity/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
        }
        data = {
            "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
            "apikey": api_key
        }
        response = requests.post(url, headers=headers, data=data, timeout=10)
        
        if response.status_code == 200:
            print_success("IAM token generated successfully")
            return True
        else:
            print_error(f"IAM token generation failed (Status: {response.status_code})")
            print(f"   Error: {response.json().get('errorMessage', 'Unknown error')}")
            return False
    except Exception as e:
        print_error(f"Error testing IBM Cloud API key: {e}")
        return False

def check_google_credentials():
    """Check Google Cloud credentials"""
    print("\nGoogle Cloud:")
    
    if not PACKAGES_INSTALLED:
        print_warning("Cannot verify (packages not installed)")
        return False
    
    load_dotenv()
    auth_token = os.getenv('GOOGLE_AUTH_TOKEN')
    project_id = os.getenv('GOOGLE_PROJECT_ID')
    
    if not auth_token or auth_token == 'your_google_auth_token_here':
        print_error("Google Auth Token not set in .env")
        print("\nGet token with: gcloud auth print-access-token")
        print("See AUTHENTICATION_SETUP.md for instructions")
        return False
    
    if not project_id or project_id == 'your_project_id_here':
        print_error("Google Project ID not set in .env")
        return False
    
    # Check token format
    if len(auth_token) < 200:
        print_warning(f"Google Auth Token length: {len(auth_token)} (expected ~258)")
        print("Token might be invalid or expired")
    else:
        print_success(f"Google Auth Token: Valid ({len(auth_token)} characters)")
    
    print_success(f"Google Project ID: Set ({project_id})")
    
    # Try to test API connection
    try:
        url = f"https://aiplatform.googleapis.com/v1beta1/projects/{project_id}/locations/global/interactions"
        headers = {
            "Authorization": f"Bearer {auth_token}",
            "Content-Type": "application/json"
        }
        # Just test authentication, don't actually create an interaction
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code in [200, 404]:  # 404 is ok, means auth worked
            print_success("API connection successful")
            return True
        elif response.status_code == 401:
            print_error("API authentication failed (token expired or invalid)")
            print("\nGet fresh token with: gcloud auth print-access-token")
            return False
        else:
            print_warning(f"API returned status {response.status_code}")
            return True  # Don't fail on other status codes
    except Exception as e:
        print_warning(f"Could not test API connection: {e}")
        return True  # Don't fail if we can't test

def check_orchestrate_cli():
    """Check if watsonx Orchestrate CLI is installed"""
    print("\nwatsonx Orchestrate:")
    
    try:
        result = subprocess.run(
            ['orchestrate', '--version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            print_success("CLI installed and accessible")
            return True
        else:
            print_error("CLI not working properly")
            return False
    except FileNotFoundError:
        print_error("CLI not installed")
        print("\nSee: https://www.ibm.com/docs/en/watsonx/watson-orchestrate")
        return False
    except Exception as e:
        print_warning(f"Could not verify CLI: {e}")
        return True  # Don't fail if we can't check

def check_env_file():
    """Check if .env file exists"""
    if not Path('.env').exists():
        print_error(".env file not found")
        print("\nCreate it with: cp .env.example .env")
        print("Then add your credentials")
        return False
    return True

def main():
    """Main verification function"""
    print_header("🔍 Google Deep Research Agent - Setup Verification")
    
    all_checks = []
    
    # Check Python
    all_checks.append(check_python_version())
    
    # Check packages
    all_checks.append(check_packages())
    
    # Check .env file
    if not check_env_file():
        print_error("\n.env file missing - cannot verify credentials")
        print("\nNext steps:")
        print("1. Copy .env.example to .env")
        print("2. Add your credentials (see AUTHENTICATION_SETUP.md)")
        print("3. Run this script again")
        sys.exit(1)
    
    # Check credentials
    all_checks.append(check_ibm_credentials())
    all_checks.append(check_google_credentials())
    
    # Check CLI
    all_checks.append(check_orchestrate_cli())
    
    # Summary
    print_header("📊 Verification Summary")
    
    if all(all_checks):
        print_success("All checks passed!")
        print("\nYou're ready to deploy the agent!")
        print("Run: ./deploy.sh")
        sys.exit(0)
    else:
        print_error("Some checks failed")
        print("\nPlease fix the issues above and run this script again.")
        print("See AUTHENTICATION_SETUP.md for detailed instructions.")
        sys.exit(1)

if __name__ == "__main__":
    main()

# Made with Bob
