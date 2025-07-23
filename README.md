![WhatsApp Image 2025-07-23 at 19 25 01_0b20fe63](https://github.com/user-attachments/assets/68ef8b5a-01fb-4e62-9e68-897b477eebad)# Clone-GPT
# 🤖 CloneGPT

**CloneGPT** is a simple chatbot interface built using [Streamlit](https://streamlit.io/) and powered by Google's [Gemini 1.5 Flash API](https://ai.google.dev/). It allows users to interact with an AI assistant in a chat-style interface.
---

## 🚀 Features

- Chat interface using Streamlit’s new `st.chat_message` components.
- Seamless conversation history management.
- Integration with Gemini 1.5 Flash (Google's Generative Language API).

---

## 📸 Screenshot

 ![WhatsApp Image 2025-07-23 at 19 25 01_0b20fe63](https://github.com/user-attachments/assets/ed127553-2cc7-4755-9959-18a79cd2d25a)

*Simple and clean chat interface*

---

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- Streamlit
- `requests` library

### Setup

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/clonegpt.git
cd clonegpt

### Install dependencies

pip install streamlit requests

## Run the App

streamlit run app.py

## API Key

You’ll need a valid Google Generative Language API key.
Update the following line in the script with your own key:
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=YOUR_API_KEY_HERE"
Get an API key from: https://makersuite.google.com/app

### Contributing
Pull requests are welcome! For major changes, please open an issue first.

