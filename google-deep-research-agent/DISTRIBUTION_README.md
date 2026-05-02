# 🎁 Google Deep Research Agent - Distribution Package

## Welcome!

This is a **complete, ready-to-use package** for deploying Google Deep Research as a native agent in watsonx Orchestrate.

## 🚀 Get Started in 5 Minutes

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set up credentials
cp .env.example .env
# Edit .env with your IBM Cloud and Google Cloud credentials

# 3. Verify everything is configured correctly
./verify_setup.py

# 4. Deploy the agent
./deploy.sh
```

That's it! Your agent is now ready to use in watsonx Orchestrate.

## 📚 Documentation

Choose your path:

### 🏃 Quick Start (5 minutes)
→ [`QUICK_START.md`](QUICK_START.md) - Get up and running fast

### 🔑 Need Help with Credentials?
→ [`AUTHENTICATION_SETUP.md`](AUTHENTICATION_SETUP.md) - Step-by-step credential guide

### 📖 Want Complete Details?
→ [`README.md`](README.md) - Full documentation

### 📦 Package Overview
→ [`PACKAGE_SUMMARY.md`](PACKAGE_SUMMARY.md) - What's included and how it works

## ✅ What You Get

- **Working Agent**: Fully functional Google Deep Research integration
- **Automated Scripts**: One-command deployment and verification
- **Complete Documentation**: Everything you need to know
- **Security Built-in**: Credential protection and validation
- **Production Ready**: Tested and ready to use

## 🎯 What This Agent Does

Ask complex research questions and get comprehensive answers with citations:

- "Research the latest trends in artificial intelligence for 2025"
- "What are the current developments in quantum computing?"
- "Analyze the impact of climate change on agriculture"

The agent will:
- ✅ Search multiple authoritative sources
- ✅ Provide detailed, comprehensive answers
- ✅ Include citations and source links
- ✅ Handle complex research queries

## 📋 Prerequisites

Before you start, make sure you have:

- [ ] Python 3.8 or higher
- [ ] IBM Cloud account with watsonx Orchestrate access
- [ ] Google Cloud account with Deep Research API enabled
- [ ] `gcloud` CLI installed and authenticated
- [ ] `orchestrate` CLI installed

## 🛠️ Included Tools

### Verification Script
```bash
./verify_setup.py
```
Checks all prerequisites and credentials before deployment.

### API Test Script
```bash
./test_api.py
```
Tests your Google Cloud connection with a real research query.

### Deployment Script
```bash
./deploy.sh
```
Automatically deploys both the tool and agent to watsonx Orchestrate.

## 📁 Package Contents

```
google-deep-research-agent/
├── 📄 Documentation
│   ├── README.md                    # Complete guide
│   ├── QUICK_START.md              # 5-minute setup
│   ├── AUTHENTICATION_SETUP.md      # Credential guide
│   ├── PACKAGE_SUMMARY.md          # Package overview
│   └── DISTRIBUTION_README.md      # This file
│
├── ⚙️ Configuration
│   ├── .env.example                # Template (copy to .env)
│   ├── .gitignore                  # Protects credentials
│   └── requirements.txt            # Python dependencies
│
├── 🔧 Scripts
│   ├── deploy.sh                   # Deploy agent
│   ├── verify_setup.py             # Verify setup
│   └── test_api.py                 # Test API
│
├── 🤖 Agent Components
│   ├── tools/
│   │   └── deep_research_query_tool.py
│   └── agents/
│       └── deep_research_agent.yaml
```

## 🔒 Security

- Credentials stored in `.env` (never committed to git)
- `.gitignore` configured to protect sensitive files
- Scripts validate credential formats
- No hardcoded secrets in code

## 🆘 Need Help?

### Common Issues

**"Error getting IBM_IAM Token"**
- Make sure you're using an IBM Cloud API key (44 characters)
- Not a Watson Assistant key (124 characters)
- Get it from: https://cloud.ibm.com/iam/apikeys

**"Token expired"**
- Google tokens expire after 1 hour
- Get fresh token: `gcloud auth print-access-token`
- Update your `.env` file

**"Permission denied"**
- Ensure Deep Research API is enabled in Google Cloud
- Check your project permissions

### Troubleshooting Steps

1. Run `./verify_setup.py` to identify issues
2. Check [`AUTHENTICATION_SETUP.md`](AUTHENTICATION_SETUP.md) for credential help
3. Review error messages - scripts provide detailed feedback

## 🎉 Success!

You'll know everything is working when:

1. ✅ `./verify_setup.py` passes all checks
2. ✅ `./test_api.py` returns research results with citations
3. ✅ `./deploy.sh` completes without errors
4. ✅ Agent appears in your watsonx Orchestrate workspace
5. ✅ Agent responds to your research queries

## 📞 Resources

- **IBM watsonx Orchestrate Docs**: https://www.ibm.com/docs/en/watsonx/watson-orchestrate
- **Google Deep Research API**: https://cloud.google.com/vertex-ai/docs
- **IBM Cloud API Keys**: https://cloud.ibm.com/iam/apikeys
- **Google Cloud Console**: https://console.cloud.google.com

## 💡 Tips

- Keep your `.env` file secure and never commit it
- Google tokens expire hourly - refresh as needed
- Use `verify_setup.py` before deploying to catch issues early
- Test with `test_api.py` to ensure API connectivity

---

**Ready to start?** → Open [`QUICK_START.md`](QUICK_START.md) and follow the 5-minute guide!

**Version**: 1.0 | **Status**: Production Ready ✅