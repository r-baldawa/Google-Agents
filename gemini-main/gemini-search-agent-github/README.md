# Gemini Search Agent for watsonx Orchestrate

A production-ready AI agent powered by Google Gemini 2.5 Pro with real-time web search capabilities for IBM watsonx Orchestrate.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## 🌟 Features

- ✅ **Real-time Web Search** - Access current information from the web using Google Search grounding
- ✅ **Gemini 2.5 Pro** - Powered by Google's latest and most capable model
- ✅ **Single Unified Tool** - One tool handles all search needs (news, facts, general queries)
- ✅ **Easy Deployment** - Automated setup script included
- ✅ **Production Ready** - Tested and optimized for watsonx Orchestrate

## 📋 Prerequisites

Before you begin, ensure you have:

- watsonx Orchestrate account with CLI installed
- Python 3.8 or higher
- pip package manager
- Google API key with Gemini API access

## 🔑 Step 1: Get Your Google API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key

## ⚙️ Step 2: Configure API Key

**IMPORTANT:** You must update your API key in these 3 files before deploying:

### File 1: Tool Configuration
**Path:** `gemini-search-agent/tools/search_web/google_search_tool.py`

**Line 51:** Replace `YOUR_GOOGLE_API_KEY_HERE` with your actual API key

```python
# TODO: Replace with your Google API key
# Get your API key from: https://aistudio.google.com/app/apikey
api_key = 'YOUR_GOOGLE_API_KEY_HERE'  # ← Update this line
```

### File 2: Connection Configuration
**Path:** `gemini-search-agent/connections/google_credentials.yaml`

**Line 10:** Replace `YOUR_GOOGLE_API_KEY_HERE` with your actual API key

```yaml
values:
  # TODO: Replace with your Google API key
  # Get your API key from: https://aistudio.google.com/app/apikey
  api_key: YOUR_GOOGLE_API_KEY_HERE  # ← Update this line
```

### File 3: Model Configuration
**Path:** `gemini-search-agent/models/gemini-3.1-pro-preview.yaml`

**Line 23:** Replace `YOUR_GOOGLE_API_KEY_HERE` with your actual API key

```yaml
provider_config:
  provider: google
  # TODO: Replace with your Google API key
  # Get your API key from: https://aistudio.google.com/app/apikey
  api_key: YOUR_GOOGLE_API_KEY_HERE  # ← Update this line
```

## 🚀 Step 3: Deploy to Orchestrate

### Quick Start (Automated)

```bash
# 1. Clone this repository
git clone <your-repo-url>
cd gemini-search-agent-github

# 2. Update API keys in the 3 files above

# 3. Run the setup script
chmod +x setup_gemini_search_agent.sh
./setup_gemini_search_agent.sh
```

### Manual Deployment

If you prefer manual deployment:

```bash
# Install Python dependencies
pip3 install google-genai>=0.2.0 ibm-watsonx-orchestrate>=2.5.1

# Import connection
orchestrate connections import --file gemini-search-agent/connections/google_credentials.yaml

# Import model
orchestrate models import --file gemini-search-agent/models/gemini-3.1-pro-preview.yaml

# Import tool
orchestrate tools import --kind python --file gemini-search-agent/tools/search_web/google_search_tool.py

# Import agent
orchestrate agents import --file gemini-search-agent/agents/native/GeminiSearchAgent.yaml
```

## 🧪 Step 4: Test Your Agent

Go to watsonx Orchestrate UI and try these queries:

```
What are today's top news stories?
What is the current price of Bitcoin?
What are the latest developments in artificial intelligence?
Is it true that the Great Wall of China is visible from space?
```

## 📁 Repository Structure

```
gemini-search-agent-github/
├── README.md                           # This file
├── LICENSE                             # MIT License
├── .gitignore                          # Git ignore file
├── setup_gemini_search_agent.sh        # Automated setup script
└── gemini-search-agent/
    ├── agents/native/
    │   └── GeminiSearchAgent.yaml      # Agent configuration
    ├── tools/search_web/
    │   ├── google_search_tool.py       # Search tool (UPDATE API KEY HERE)
    │   └── requirements.txt            # Python dependencies
    ├── models/
    │   └── gemini-3.1-pro-preview.yaml # Model config (UPDATE API KEY HERE)
    ├── connections/
    │   └── google_credentials.yaml     # Connection (UPDATE API KEY HERE)
    └── requirements.txt                # Main dependencies
```

## 🛠️ What the Agent Can Do

The `search_web` tool can handle:

- **Current Events:** "What's happening in the world today?"
- **News Queries:** "Latest news about climate change"
- **Fact Checking:** "Is coffee bad for your health?"
- **Real-time Data:** "Current price of Tesla stock"
- **Research:** "Explain quantum computing breakthroughs"

## 🔒 Security Notes

- **Never commit your API key** to version control
- The `.gitignore` file is configured to exclude sensitive files
- Rotate your API key periodically
- Monitor your API usage in Google Cloud Console

## 📊 API Usage

Monitor your Google API usage:
- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Navigate to APIs & Services > Dashboard
- View Gemini API usage and quota

## 🐛 Troubleshooting

### "Error: Google API key not configured"
- Ensure you've updated the API key in all 3 files
- Check that the API key is valid and active

### "Failed to import tool"
- Install dependencies: `pip3 install google-genai ibm-watsonx-orchestrate`
- Verify Orchestrate CLI is installed: `orchestrate --version`

### Agent doesn't use web search
- Verify the tool is imported: `orchestrate tools list`
- Check agent configuration includes `search_web` tool

## 📝 Requirements

### Python Packages
- `google-genai>=0.2.0` - Google Generative AI SDK
- `ibm-watsonx-orchestrate>=2.5.1` - Orchestrate SDK

### Google API
- Active Google Cloud account
- Gemini API access enabled
- Valid API key with sufficient quota

### Orchestrate
- watsonx Orchestrate account
- CLI installed and configured
- Permissions to import agents, tools, and models

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built for IBM watsonx Orchestrate
- Powered by Google Gemini 2.5 Pro
- Uses Google Search grounding for real-time information

## 📧 Support

For issues or questions:
- Open an issue in this repository
- Check the troubleshooting section above
- Review watsonx Orchestrate documentation

## 🎯 Quick Checklist

Before deploying, make sure you've:

- [ ] Obtained a Google API key
- [ ] Updated API key in `tools/search_web/google_search_tool.py` (line 51)
- [ ] Updated API key in `connections/google_credentials.yaml` (line 10)
- [ ] Updated API key in `models/gemini-3.1-pro-preview.yaml` (line 23)
- [ ] Installed Python dependencies
- [ ] Configured Orchestrate CLI
- [ ] Run the setup script or manual deployment commands

---

**Ready to deploy?** Follow the steps above and start using your Gemini Search Agent! 🚀