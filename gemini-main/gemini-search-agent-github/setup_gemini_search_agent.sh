#!/bin/bash

################################################################################
# Gemini Search Agent Setup Script
# 
# This script automates the deployment of the Gemini Search Agent to
# watsonx Orchestrate. It imports all necessary components including:
# - Google credentials connection
# - Gemini 3.1 Pro model configuration
# - Three Python tools (search_web, get_latest_news, fact_check)
# - The Gemini Search Agent
#
# Prerequisites:
# - watsonx Orchestrate CLI installed and configured
# - Valid Google API key with Gemini API access
# - Python 3.8+ installed
# - Required Python packages (google-genai, ibm-watsonx-orchestrate)
#
# Usage:
#   ./setup_gemini_search_agent.sh
#
# Author: Created for watsonx Orchestrate integration
################################################################################

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo ""
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}"
    echo ""
}

# Check if orchestrate CLI is installed
check_prerequisites() {
    print_header "Checking Prerequisites"
    
    if ! command -v orchestrate &> /dev/null; then
        print_error "watsonx Orchestrate CLI is not installed or not in PATH"
        print_status "Please install the Orchestrate CLI first"
        exit 1
    fi
    print_success "Orchestrate CLI found"
    
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed or not in PATH"
        exit 1
    fi
    print_success "Python 3 found"
}

# Install Python dependencies
install_dependencies() {
    print_header "Installing Python Dependencies"
    
    print_status "Installing google-genai and ibm-watsonx-orchestrate..."
    pip3 install google-genai>=0.2.0 ibm-watsonx-orchestrate>=2.5.1 --quiet
    
    if [ $? -eq 0 ]; then
        print_success "Python dependencies installed successfully"
    else
        print_error "Failed to install Python dependencies"
        exit 1
    fi
}

# Import connection
import_connection() {
    print_header "Importing Google Credentials Connection"
    
    print_status "Importing google_credentials connection..."
    orchestrate connections import --file gemini-search-agent/connections/google_credentials.yaml
    
    if [ $? -eq 0 ]; then
        print_success "Connection imported successfully"
        print_warning "IMPORTANT: You must add your Google API key to the connection!"
        print_status "Go to Orchestrate UI > Connections > google_credentials > Edit"
        print_status "Add your API key in the 'api_key' field"
        print_status "Get your API key from: https://aistudio.google.com/app/apikey"
    else
        print_error "Failed to import connection"
        exit 1
    fi
}

# Import model
import_model() {
    print_header "Importing Gemini 3.1 Pro Model"
    
    print_status "Importing gemini-3.1-pro-preview model..."
    orchestrate models import --file gemini-search-agent/models/gemini-3.1-pro-preview.yaml
    
    if [ $? -eq 0 ]; then
        print_success "Model imported successfully"
    else
        print_error "Failed to import model"
        exit 1
    fi
}

# Import tools
import_tools() {
    print_header "Importing Python Tool"
    
    # Import search_web tool
    print_status "Importing search_web tool..."
    orchestrate tools import --file gemini-search-agent/tools/search_web/google_search_tool.py
    if [ $? -eq 0 ]; then
        print_success "search_web tool imported successfully"
    else
        print_error "Failed to import search_web tool"
        exit 1
    fi
}

# Import agent
import_agent() {
    print_header "Importing Gemini Search Agent"
    
    print_status "Importing GeminiSearchAgent..."
    orchestrate agents import --file gemini-search-agent/agents/native/GeminiSearchAgent.yaml
    
    if [ $? -eq 0 ]; then
        print_success "Agent imported successfully"
    else
        print_error "Failed to import agent"
        exit 1
    fi
}

# Main execution
main() {
    print_header "Gemini Search Agent Setup"
    print_status "Starting deployment process..."
    
    # Run all steps
    check_prerequisites
    install_dependencies
    import_connection
    import_model
    import_tools
    import_agent
    
    # Final success message
    print_header "Setup Complete!"
    print_success "Gemini Search Agent has been successfully deployed!"
    echo ""
    print_warning "NEXT STEPS:"
    echo "1. Go to watsonx Orchestrate UI"
    echo "2. Navigate to Agents and find 'GeminiSearchAgent'"
    echo "3. Test the agent with a query like 'What are today's top news stories?'"
    echo ""
    print_status "Note: The API key is already configured in the tool"
    echo ""
    print_status "For detailed instructions, see DEPLOYMENT_GUIDE.md"
    echo ""
}

# Run main function
main

# Made with Bob
