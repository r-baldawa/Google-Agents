# Authentication Setup Guide

Complete step-by-step instructions for obtaining all required credentials for the Google Deep Research Agent.

## 📋 Table of Contents

- [Overview](#overview)
- [IBM Cloud API Key](#ibm-cloud-api-key)
- [Google Cloud Authentication](#google-cloud-authentication)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

You need **two** credentials to use this agent:

1. **IBM Cloud API Key** - For deploying to watsonx Orchestrate
2. **Google Cloud Auth Token** - For accessing Google Deep Research API

**Estimated time:** 10-15 minutes

---

## 🔑 IBM Cloud API Key

### What You Need
- IBM Cloud account with watsonx Orchestrate access
- Permission to create API keys

### Step-by-Step Instructions

#### 1. Login to IBM Cloud

Go to: **https://cloud.ibm.com**

- Click "Log in" (top right)
- Enter your IBM Cloud credentials
- Complete any 2FA if required

#### 2. Navigate to API Keys Page

Go to: **https://cloud.ibm.com/iam/apikeys**

Or navigate manually:
- Click your profile icon (top right)
- Select "Manage" → "Access (IAM)"
- Click "API keys" in the left sidebar

#### 3. Create New API Key

- Click the blue **"Create"** button (top right)
- Fill in the form:
  - **Name:** `watsonx-orchestrate-deep-research`
  - **Description:** `API key for Google Deep Research Agent in watsonx Orchestrate`
- Click **"Create"**

#### 4. Copy the API Key

⚠️ **CRITICAL:** You will only see this key once!

- A dialog will appear with your new API key
- Click **"Copy"** or manually select and copy the entire key
- The key should be approximately **44 characters** long
- Example format: `aBcD1234EfGh5678IjKl9012MnOp3456QrSt7890`

#### 5. Save the API Key

**Option A: Save to .env file immediately**
```bash
# Open .env file
nano .env

# Add your key
IBM_CLOUD_API_KEY=<paste-your-key-here>

# Save and exit (Ctrl+X, then Y, then Enter)
```

**Option B: Save to a secure location**
- Password manager (recommended)
- Encrypted notes
- Secure document

⚠️ **Never:**
- Share the key publicly
- Commit it to version control
- Store it in plain text files

#### 6. Verify the Key

```bash
python verify_setup.py
```

Expected output:
```
✅ IBM Cloud API Key: Valid (44 characters)
✅ IAM token generated successfully
```

### Key Format

**Correct format:**
- Length: ~44 characters
- Contains: Letters, numbers, hyphens, underscores
- Example: `1Bj_kE6Rbj_Jvhz30uAjDLWju26KnKMSEw_2zfTOzqiE`

**Incorrect formats:**
- Base64-encoded strings (124+ characters)
- Watson Assistant credentials
- Service credentials from other IBM services

### Troubleshooting

**Problem:** "I don't see the Create button"

**Solution:** You may not have permission. Contact your IBM Cloud administrator to:
- Grant you "Service ID creator" role
- Or create an API key for you

**Problem:** "I lost my API key"

**Solution:** You cannot retrieve a lost key. You must:
1. Delete the old key (if you remember which one)
2. Create a new key following steps above

**Problem:** "API key validation fails"

**Solution:**
1. Verify you copied the entire key (no spaces)
2. Check it's an IBM Cloud API key (not Watson Assistant)
3. Ensure your account has watsonx Orchestrate access

---

## 🌐 Google Cloud Authentication

### What You Need
- Google Cloud account
- Access to Deep Research API
- Google Cloud SDK installed

### Step-by-Step Instructions

#### 1. Install Google Cloud SDK

**If not already installed:**

**macOS:**
```bash
brew install google-cloud-sdk
```

**Linux:**
```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
```

**Windows:**
Download from: https://cloud.google.com/sdk/docs/install

#### 2. Login to Google Cloud

```bash
gcloud auth login
```

This will:
- Open your browser
- Ask you to select your Google account
- Request permission to access Google Cloud
- Return to terminal when complete

#### 3. Set Your Project

```bash
# List available projects
gcloud projects list

# Set your project (replace with your project ID)
gcloud config set project YOUR_PROJECT_ID
```

**Finding your Project ID:**
- Go to: https://console.cloud.google.com
- Click the project dropdown (top left)
- Your Project ID is shown next to the project name

#### 4. Get Authentication Token

```bash
gcloud auth print-access-token
```

This will output a token like:
```
ya29.a0ATkoCc5zMXznW...  (258 characters)
```

#### 5. Copy the Token

**Important notes:**
- Token is **~258 characters** long
- Token **expires after 1 hour**
- You'll need to get a new token when it expires

**Copy the entire token:**
```bash
# Copy to clipboard (macOS)
gcloud auth print-access-token | pbcopy

# Copy to clipboard (Linux with xclip)
gcloud auth print-access-token | xclip -selection clipboard

# Or manually copy from terminal
gcloud auth print-access-token
```

#### 6. Save to .env File

```bash
# Open .env file
nano .env

# Add your token
GOOGLE_AUTH_TOKEN=<paste-your-token-here>

# Add your project ID
GOOGLE_PROJECT_ID=<your-project-id>

# Save and exit (Ctrl+X, then Y, then Enter)
```

#### 7. Verify the Token

```bash
python verify_setup.py
```

Expected output:
```
✅ Google Auth Token: Valid (258 characters)
✅ Google Project ID: Set (883982946869)
✅ API connection successful
```

### Token Expiration

**Google auth tokens expire after 1 hour.**

When you see authentication errors:
```bash
# Get a fresh token
gcloud auth print-access-token

# Update .env file
nano .env
# Replace GOOGLE_AUTH_TOKEN with new token
```

### Alternative: Service Account (Advanced)

For production use, consider using a service account:

1. Create service account in Google Cloud Console
2. Download JSON key file
3. Set environment variable:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/key.json"
   ```

See: https://cloud.google.com/docs/authentication/getting-started

### Troubleshooting

**Problem:** "gcloud: command not found"

**Solution:** Install Google Cloud SDK (see Step 1)

**Problem:** "Token expired" or "401 Unauthorized"

**Solution:** Get a fresh token:
```bash
gcloud auth print-access-token
```

**Problem:** "Project not found"

**Solution:** Verify project ID:
```bash
gcloud projects list
gcloud config set project YOUR_PROJECT_ID
```

**Problem:** "Permission denied" for Deep Research API

**Solution:** 
1. Go to: https://console.cloud.google.com/apis/library
2. Search for "Vertex AI API"
3. Click "Enable"
4. Contact Google Cloud support for Deep Research API access

---

## ✅ Verification

### Complete Setup Verification

After obtaining both credentials, run:

```bash
python verify_setup.py
```

### Expected Output

```
========================================
🔍 Setup Verification
========================================

Python Environment:
✅ Python version: 3.12.0
✅ Required packages installed

IBM Cloud:
✅ IBM Cloud API Key: Valid (44 characters)
✅ IAM token generated successfully

Google Cloud:
✅ Google Auth Token: Valid (258 characters)
✅ Google Project ID: Set (883982946869)
✅ API connection successful

watsonx Orchestrate:
✅ CLI installed and accessible

========================================
✅ All checks passed!
========================================

You're ready to deploy the agent!
Run: ./deploy.sh
```

### If Verification Fails

1. **Check .env file format:**
   ```bash
   cat .env
   ```
   Ensure no extra spaces or quotes around values

2. **Verify credentials individually:**
   ```bash
   # Test IBM Cloud
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('IBM_CLOUD_API_KEY'))"
   
   # Test Google Cloud
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('GOOGLE_AUTH_TOKEN')[:20])"
   ```

3. **Re-obtain credentials:**
   - IBM Cloud: Create new API key
   - Google Cloud: Get fresh token

---

## 🔐 Security Best Practices

### Do's ✅
- Store credentials in `.env` file (gitignored)
- Use password manager for backup
- Rotate credentials regularly
- Use environment-specific keys
- Monitor usage in cloud consoles

### Don'ts ❌
- Never commit `.env` to git
- Never share credentials publicly
- Never hardcode in source files
- Never store in plain text documents
- Never use production keys for testing

### Credential Rotation

**IBM Cloud API Key:**
- Rotate every 90 days
- Create new key before deleting old one
- Update all environments

**Google Auth Token:**
- Automatically expires after 1 hour
- Get fresh token as needed
- Consider service account for production

---

## 📞 Getting Help

### IBM Cloud Support
- Documentation: https://cloud.ibm.com/docs
- Support: https://cloud.ibm.com/unifiedsupport/supportcenter
- Community: https://community.ibm.com/community/user/cloud/home

### Google Cloud Support
- Documentation: https://cloud.google.com/docs
- Support: https://cloud.google.com/support
- Community: https://www.googlecloudcommunity.com/

### watsonx Orchestrate
- Documentation: https://www.ibm.com/docs/en/watsonx/watson-orchestrate
- Contact your IBM representative

---

**Last Updated:** March 8, 2026  
**Version:** 1.0