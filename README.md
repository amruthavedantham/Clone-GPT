# 🤖 CloneGPT

**CloneGPT** is a lightweight chatbot interface built with [Streamlit](https://streamlit.io/) and powered by Google's [Gemini 1.5 Flash API](https://ai.google.dev/). It provides a smooth and interactive chat experience using modern UI components.

---

## 🚀 Features

* 💬 Chat interface using Streamlit’s `st.chat_message` component.
* 🔄 Seamless conversation history handling.
* ⚡ Integrated with Google's Gemini 1.5 Flash API for fast, intelligent responses.
* 🧠 Lightweight and easy to deploy.

---

## 📸 Screenshot

![Chat UI](https://github.com/user-attachments/assets/ed127553-2cc7-4755-9959-18a79cd2d25a)
*Simple and clean chat interface*

---

## ⚙️ Getting Started

Follow these steps to install, set up, and run the chatbot locally:

### 1. Prerequisites

Make sure you have the following installed:

* Python 3.8 or higher
* pip (Python package manager)

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/clonegpt.git
cd clonegpt
```

### 3. Install Dependencies

```bash
pip install streamlit requests
```

### 4. Set Up API Key

To access the Gemini 1.5 Flash model, you’ll need a valid API key from Google:

* Visit [Google MakerSuite](https://makersuite.google.com/app) and generate your API key.
* In `app.py`, replace the placeholder with your API key:

```python
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=YOUR_API_KEY_HERE"
```

> ⚠️ **Important**: Never share or expose your API key publicly.

### 5. Run the App

```bash
streamlit run app.py
```

The chatbot should now be live at: [http://localhost:8501](http://localhost:8501)

---

## 🤝 Contributing

Contributions are welcome!
To contribute:

* Fork the repository
* Create a new branch:

  ```bash
  git checkout -b feature-name
  ```
* Commit your changes:

  ```bash
  git commit -m "Add new feature"
  ```
* Push to the branch:

  ```bash
  git push origin feature-name
  ```
* Open a Pull Request

> 📌 Please open an issue first for any major change proposals.

---

## 🙌 Acknowledgements

This project was created as part of the **Google Developer Student Clubs (GDSC) Workshop – Building ChatGPT**.

---


## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

For questions or suggestions, feel free to open an issue or reach out via GitHub.

---
