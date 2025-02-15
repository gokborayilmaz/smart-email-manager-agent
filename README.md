# 📩 Smart Email Manager Agent - Day 17/21

This agent is part of the **Everyday New AI Agent** series - **Day 17/21** 🚀

## 📌 Overview

The **Smart Email Manager Agent** is designed to analyze emails and extract useful information using **Upsonic AI**.

### 🔹 Features:
- ✨ **Summarizes** the key points of an email.
- ✅ **Identifies action items** and tasks within the email.
- 📅 **Extracts meetings and event details** for scheduling.
- ✉️ **Suggests a professional response** if needed.
- ⚡ **FastAPI-based UI** for easy interaction.

---

## 🛠️ Installation & Setup

### **Prerequisites**
- Python 3.9 or higher
- Git
- Virtual environment (recommended)
- **Azure OpenAI API Key** (for AI processing)

### **Installation**

1️⃣ Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

3️⃣ Set up your environment variables:
Create a `.env` file in the root directory and configure it as follows:

```env
AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
AZURE_OPENAI_ENDPOINT="your_azure_openai_endpoint"
AZURE_OPENAI_API_VERSION="your_azure_openai_api_version"
```

---

## 🚀 Running the Application

Start the FastAPI server:

```bash
uvicorn upsonicai:app --reload
```

Open the UI in your browser:

```
http://127.0.0.1:8000/
```

---

## 🔗 API Endpoints

### **1️⃣ Analyze Email**

- **Endpoint:** `GET /analyze_email`
- **Query Parameters:**
  - `email` (string) - The full email content to be analyzed.
- **Example Usage:**

```bash
curl "http://127.0.0.1:8000/analyze_email?email=Your%20email%20content%20here"
```

- **Response:**

```json
{
  "summary": "Project planning meeting scheduled for Feb 15.",
  "tasks": [
    "Finalize reports on development areas by Feb 15",
    "Prepare wireframe presentation",
    "Schedule a meeting with the finance team"
  ],
  "events": [
    "Project planning meeting on Feb 15 at 14:00 GMT+3"
  ],
  "suggested_reply": "Thank you for your email. I will prepare the requested documents and join the meeting on Feb 15."
}
```

---

🔗 **Explore More:** [GitHub Repository](https://github.com/your-repo-url)

🚀 **UpsonicAI - Making AI Agents Simple & Scalable!**

