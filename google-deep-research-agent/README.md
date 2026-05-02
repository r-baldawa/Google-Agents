# Google Deep Research Agent for watsonx Orchestrate

A production-ready AI agent that integrates Google's Deep Research capabilities into IBM watsonx Orchestrate, enabling comprehensive research on any topic through a simple chat interface.

## 📋 Table of Contents

- [What This Agent Does](#what-this-agent-does)
- [Quick Start](#quick-start)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Support](#support)

---

## 🎯 What This Agent Does

The Deep Research Agent:
- **Accepts questions** from users through watsonx Orchestrate chat UI
- **Searches multiple sources** using Google's Deep Research AI
- **Synthesizes information** from authoritative sources
- **Provides detailed findings** with proper citations
- **Returns structured responses** formatted for easy reading

### Example Use Cases
- Market research and competitive analysis
- Technical documentation research
- Academic literature reviews
- Current events and news analysis
- Product feature comparisons
- Industry trend analysis

---

## 🚀 Quick Start

**Time to deploy:** ~15 minutes

1. **Get credentials** (see [AUTHENTICATION_SETUP.md](AUTHENTICATION_SETUP.md))
   - IBM Cloud API key
   - Google Cloud authentication token

2. **Configure** (see [Configuration](#configuration))
   - Copy `.env.example` to `.env`
   - Add your credentials

3. **Verify setup** (see [Installation](#installation))
   ```bash
   python verify_setup.py
   ```

4. **Deploy** (see [Deployment](#deployment))
   ```bash
   ./deploy.sh
   ```

5. **Use** in watsonx Orchestrate chat UI!

---

## 📦 Prerequisites

### Required Software
- **Python 3.8+** - [Download](https://www.python.org/downloads/)
- **watsonx Orchestrate CLI** - [Installation Guide](https://www.ibm.com/docs/en/watsonx/watson-orchestrate)
- **Google Cloud SDK** (for getting auth token) - [Download](https://cloud.google.com/sdk/docs/install)

### Required Accounts
- **IBM Cloud Account** - [Sign up](https://cloud.ibm.com/registration)
- **watsonx Orchestrate Access** - Contact your IBM representative
- **Google Cloud Account** with Deep Research API access - [Sign up](https://cloud.google.com/)

### Required Permissions
- IBM Cloud: Ability to create API keys
- watsonx Orchestrate: Ability to import tools and agents
- Google Cloud: Access to Deep Research API

---

## 💻 Installation

### Step 1: Clone or Download This Package

If you received this as a ZIP file, extract it. Otherwise:
```bash
git clone <repository-url>
cd google-deep-research-agent
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

**Required packages:**
- `requests` - For API calls
- `python-dotenv` - For environment variable management
- `ibm-watsonx-orchestrate` - For agent deployment

### Step 3: Verify Installation

```bash
python verify_setup.py
```

This will check:
- ✅ Python version
- ✅ Required packages installed
- ✅ watsonx Orchestrate CLI available
- ✅ Google Cloud SDK available (optional)

---

## ⚙️ Configuration

### Step 1: Create Environment File

```bash
cp .env.example .env
```

### Step 2: Add Your Credentials

Edit `.env` and add your credentials:

```bash
# IBM Cloud API Key (REQUIRED)
# Get from: https://cloud.ibm.com/iam/apikeys
IBM_CLOUD_API_KEY=your_ibm_cloud_api_key_here

# Google Cloud Auth Token (REQUIRED)
# Get by running: gcloud auth print-access-token
GOOGLE_AUTH_TOKEN=your_google_auth_token_here

# Google Cloud Project ID (REQUIRED)
# Find in Google Cloud Console
GOOGLE_PROJECT_ID=your_project_id_here
```

### Step 3: Verify Configuration

```bash
python verify_setup.py
```

Expected output:
```
✅ IBM Cloud API Key: Valid
✅ Google Auth Token: Valid
✅ Google Project ID: Set
✅ All credentials verified!
```

**Need help getting credentials?** See [AUTHENTICATION_SETUP.md](AUTHENTICATION_SETUP.md) for detailed instructions.

---

## 🚀 Deployment

### Step 1: Authenticate with watsonx Orchestrate

```bash
# List available environments
orchestrate env list

# Activate your environment
orchestrate env activate <your-environment-name>
```

### Step 2: Deploy the Agent

```bash
./deploy.sh
```

This script will:
1. Import the `deep_research_query` tool
2. Import the `deep_research_agent` agent
3. Verify successful deployment

Expected output:
```
========================================
Deploying Deep Research Agent
========================================

✅ Tool imported successfully
✅ Agent imported successfully
✅ Deployment Complete!
```

### Step 3: Verify Deployment

```bash
# List imported tools
orchestrate tools list | grep deep_research

# List imported agents
orchestrate agents list | grep deep_research
```

---

## 💬 Usage

### In watsonx Orchestrate Chat UI

1. **Open** watsonx Orchestrate
2. **Start** a new chat
3. **Type** `@deep_research_agent` or select it from the agent list
4. **Ask** your research question

### Example Questions

**Starter Prompts** (built into the agent):
- "Research the latest trends in artificial intelligence for 2025"
- "What are the key features of IBM watsonx Orchestrate?"
- "Analyze the competitive landscape for cloud computing services"
- "Research best practices for implementing AI agents in enterprise"

**Custom Questions:**
- "What are the environmental impacts of electric vehicles?"
- "Compare the top 5 project management tools for 2025"
- "What are the latest developments in quantum computing?"
- "Research the history and evolution of artificial intelligence"

### Response Format

The agent returns:
```
# Research Summary

## Key Findings
1. [Finding with citation]
2. [Finding with citation]
3. [Finding with citation]

## Detailed Analysis
[Comprehensive research with multiple citations]

## Sources
[List of authoritative sources used]
```

---

## 🔧 Troubleshooting

### Common Issues

#### 1. "Authentication token not found"

**Problem:** Google auth token is missing or expired

**Solution:**
```bash
# Get a fresh token (expires after 1 hour)
gcloud auth print-access-token

# Update .env file with new token
nano .env
```

#### 2. "IBM Cloud API key invalid"

**Problem:** API key is incorrect or expired

**Solution:**
1. Go to https://cloud.ibm.com/iam/apikeys
2. Create a new API key
3. Update `.env` file
4. Run `python verify_setup.py` to confirm

#### 3. "Tool import failed"

**Problem:** Not authenticated with watsonx Orchestrate

**Solution:**
```bash
orchestrate env activate <your-environment>
./deploy.sh
```

#### 4. "Module not found" error in watsonx Orchestrate

**Problem:** This was fixed in the current version

**Solution:** Re-deploy the agent:
```bash
./deploy.sh
```

### Getting Help

1. **Check logs:** Review deployment output for specific errors
2. **Verify credentials:** Run `python verify_setup.py`
3. **Review documentation:** See [AUTHENTICATION_SETUP.md](AUTHENTICATION_SETUP.md)
4. **Test API:** Run `python test_api.py` to test Google Deep Research API

---

## 📁 File Structure

```
google-deep-research-agent/
├── README.md                          # This file
├── AUTHENTICATION_SETUP.md            # Detailed credential setup guide
├── requirements.txt                   # Python dependencies
├── .env.example                       # Environment template
├── deploy.sh                          # Deployment script
├── verify_setup.py                    # Setup verification script
├── test_api.py                        # API testing script
├── tools/
│   └── deep_research_query_tool.py   # Main tool implementation
└── agents/
    └── deep_research_agent.yaml      # Agent configuration
```

---

## 🔐 Security Notes

- **Never commit** `.env` file to version control
- **Rotate credentials** regularly
- **Use environment-specific** API keys
- **Limit permissions** to minimum required
- **Monitor usage** through IBM Cloud and Google Cloud consoles

---

## 📝 License

This agent is provided as-is for use with IBM watsonx Orchestrate and Google Cloud services.

---

## 🤝 Support

For issues or questions:
1. Review [AUTHENTICATION_SETUP.md](AUTHENTICATION_SETUP.md)
2. Run `python verify_setup.py` for diagnostics
3. Check [Troubleshooting](#troubleshooting) section
4. Contact your IBM watsonx Orchestrate administrator

---

**Version:** 1.0  
**Last Updated:** March 8, 2026  
**Status:** Production Ready ✅