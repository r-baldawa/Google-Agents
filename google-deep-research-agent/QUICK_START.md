# Quick Start Guide

Get up and running with the Google Deep Research Agent in 5 minutes!

## Prerequisites Checklist

- [ ] Python 3.8 or higher installed
- [ ] IBM Cloud account with watsonx Orchestrate access
- [ ] Google Cloud account with Deep Research API enabled
- [ ] `gcloud` CLI installed and authenticated
- [ ] `orchestrate` CLI installed

## Setup Steps

### 1. Install Dependencies (1 minute)

```bash
pip install -r requirements.txt
```

### 2. Configure Credentials (2 minutes)

```bash
# Copy the template
cp .env.example .env

# Edit .env and add your credentials
# See AUTHENTICATION_SETUP.md for detailed instructions
```

You need:
- **IBM Cloud API Key** (44 characters) - Get from: https://cloud.ibm.com/iam/apikeys
- **Google Auth Token** (258 characters) - Get with: `gcloud auth print-access-token`
- **Google Project ID** - Get from: `gcloud config get-value project`

### 3. Verify Setup (1 minute)

```bash
./verify_setup.py
```

This checks:
- ✅ Python version
- ✅ Required packages
- ✅ IBM Cloud credentials
- ✅ Google Cloud credentials
- ✅ watsonx Orchestrate CLI

### 4. Test API Connection (Optional, 1 minute)

```bash
./test_api.py
```

This runs a test query to verify your Google Cloud credentials work.

### 5. Deploy Agent (1 minute)

```bash
./deploy.sh
```

This will:
1. Deploy the Deep Research tool
2. Deploy the Deep Research agent
3. Verify deployment success

## Usage

Once deployed, you can use the agent in watsonx Orchestrate:

1. Open watsonx Orchestrate
2. Find "Deep Research Agent" in your agents
3. Ask questions like:
   - "Research the latest trends in artificial intelligence"
   - "What are the current developments in quantum computing?"
   - "Analyze the impact of climate change on agriculture"

The agent will:
- Conduct comprehensive research across multiple sources
- Provide detailed answers with citations
- Include links to source materials

## Troubleshooting

### Token Expired Error
Google auth tokens expire after 1 hour. Get a fresh token:
```bash
gcloud auth print-access-token
```
Update your `.env` file with the new token.

### IBM IAM Token Error
Make sure you're using an IBM Cloud API key (44 characters), not a Watson Assistant key.

### Deployment Failed
Run the verification script to identify issues:
```bash
./verify_setup.py
```

## Next Steps

- Read [AUTHENTICATION_SETUP.md](AUTHENTICATION_SETUP.md) for detailed credential instructions
- Read [README.md](README.md) for complete documentation
- Check [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) for common issues

## Support

For issues or questions:
1. Check the troubleshooting guides
2. Review the authentication setup documentation
3. Verify all prerequisites are met

## File Structure

```
google-deep-research-agent/
├── README.md                    # Complete documentation
├── AUTHENTICATION_SETUP.md      # Detailed credential guide
├── QUICK_START.md              # This file
├── .env.example                # Environment template
├── .gitignore                  # Git ignore rules
├── requirements.txt            # Python dependencies
├── deploy.sh                   # Deployment script
├── verify_setup.py             # Setup verification
├── test_api.py                 # API test script
├── tools/
│   └── deep_research_query_tool.py
└── agents/
    └── deep_research_agent.yaml
```

---

**Ready to deploy?** Run `./deploy.sh` and start researching! 🚀