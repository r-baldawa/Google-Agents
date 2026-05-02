#!/usr/bin/env bash

# Google Deep Research Agent - Deployment Script
# This script deploys the agent to watsonx Orchestrate

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;36m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo ""
echo "========================================"
echo "🚀 Deploying Google Deep Research Agent"
echo "========================================"
echo ""

# Check if .env file exists
if [ ! -f "${SCRIPT_DIR}/.env" ]; then
    echo -e "${RED}❌ Error: .env file not found${NC}"
    echo ""
    echo "Please create .env file from .env.example:"
    echo "  cp .env.example .env"
    echo ""
    echo "Then add your credentials. See AUTHENTICATION_SETUP.md for help."
    exit 1
fi

# Check if orchestrate CLI is available
if ! command -v orchestrate &> /dev/null; then
    echo -e "${RED}❌ Error: orchestrate CLI not found${NC}"
    echo ""
    echo "Please install watsonx Orchestrate CLI first."
    echo "See: https://www.ibm.com/docs/en/watsonx/watson-orchestrate"
    exit 1
fi

# Check current environment
echo -e "${BLUE}📋 Checking watsonx Orchestrate environment...${NC}"
CURRENT_ENV=$(orchestrate env list 2>/dev/null | grep "active" | awk '{print $2}' || echo "none")

if [ "$CURRENT_ENV" = "none" ]; then
    echo -e "${YELLOW}⚠️  No active environment detected${NC}"
    echo ""
    echo "Please activate an environment first:"
    echo "  orchestrate env list"
    echo "  orchestrate env activate <environment-name>"
    echo ""
    exit 1
fi

echo -e "${GREEN}✅ Active environment: ${CURRENT_ENV}${NC}"
echo ""

# Import Python tool
echo -e "${BLUE}📦 Importing Python tool: deep_research_query_tool.py${NC}"
if orchestrate tools import -k python -f "${SCRIPT_DIR}/tools/deep_research_query_tool.py" --app-id vertex_oauth_code; then
    echo -e "${GREEN}✅ Tool imported successfully${NC}"
else
    echo -e "${RED}❌ Tool import failed${NC}"
    echo ""
    echo "Troubleshooting:"
    echo "1. Verify you're authenticated: orchestrate env list"
    echo "2. Check tool file exists: ls tools/deep_research_query_tool.py"
    echo "3. Ensure connection 'vertex_oauth_code' exists in watsonx Orchestrate"
    echo "4. Review error message above"
    exit 1
fi

echo ""

# Import agent
echo -e "${BLUE}🤖 Importing agent: deep_research_agent.yaml${NC}"
if orchestrate agents import -f "${SCRIPT_DIR}/agents/deep_research_agent.yaml"; then
    echo -e "${GREEN}✅ Agent imported successfully${NC}"
else
    echo -e "${RED}❌ Agent import failed${NC}"
    echo ""
    echo "Troubleshooting:"
    echo "1. Verify tool was imported successfully (see above)"
    echo "2. Check agent file exists: ls agents/deep_research_agent.yaml"
    echo "3. Review error message above"
    exit 1
fi

echo ""
echo "========================================"
echo -e "${GREEN}✅ Deployment Complete!${NC}"
echo "========================================"
echo ""
echo "The Deep Research Agent is now available in watsonx Orchestrate."
echo ""
echo "To use it:"
echo "1. Open watsonx Orchestrate chat UI"
echo "2. Type: @deep_research_agent"
echo "3. Ask your research question"
echo ""
echo "Example questions:"
echo "  - Research the latest trends in AI for 2025"
echo "  - What are the key features of IBM watsonx?"
echo "  - Analyze the competitive landscape for cloud services"
echo ""
echo "Environment: ${CURRENT_ENV}"
echo ""

# Made with Bob
