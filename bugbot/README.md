# 🐛 BugBot

**BugBot** is an AI-powered Python debugging assistant that transforms your natural language prompts into executable Python code, runs it, and automatically fixes errors—helping you build and debug faster than ever.

---

## 🚀 What is BugBot?

BugBot is an interactive Streamlit app that leverages LLMs (via Groq) to:
- **Generate Python code** from your instructions
- **Extract function parameters** and prompt you for inputs
- **Execute code in real time** and display results
- **Detect and fix errors automatically** (including missing modules)
- **Iterate with feedback loops** until your code runs successfully

---

## ✨ Features

- 📝 **Prompt-to-Code:** Enter a natural language prompt and instantly get dynamic, ready-to-run Python code.
- 🧠 **Smart Input Handling:** BugBot analyzes generated functions and asks for any required parameters.
- ⚡ **One-Click Execution:** Run your code directly in the app and see output or errors immediately.
- 🔄 **Self-Healing:** If errors occur, BugBot attempts to fix them automatically using LLM-powered code repair.
- 📦 **Auto Module Installer:** Missing a Python package? BugBot detects and installs it for you.
- 🛡️ **Error Explanations:** Friendly, actionable error messages and suggestions.
- 🖥️ **Modern UI:** Clean, responsive interface built with Streamlit and custom CSS.

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) — UI and app framework
- [Groq](https://groq.com/) — LLM API for code generation and repair
- [Python 3.8+](https://www.python.org/)
- [dotenv](https://pypi.org/project/python-dotenv/) — For API key management

---

## 🏁 Getting Started

1. **Clone the repo:**
    ```bash
    git clone https://github.com/sarakhan7/BugBot.git
    cd BugBot/bugbot
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your environment:**
    - Create a `.env` file in `bugbot/src/` with your Groq API key:
      ```
      GROQ_API_KEY=your_groq_api_key_here
      ```

4. **Run BugBot:**
    ```bash
    streamlit run src/app.py
    ```

---

## 🖼️ Screenshots

![BugBot UI Screenshot](![image](https://github.com/user-attachments/assets/1bb6ef5c-3276-452c-a631-908b73d10034)
)

---

## 🤖 How It Works

1. **Prompt:** Enter a description of the Python function or script you want.
2. **Code Generation:** BugBot uses LLMs to generate Python code.
3. **Parameter Extraction:** It finds required function parameters and asks you for values.
4. **Execution:** Runs the code and displays output or errors.
5. **Self-Healing:** If errors are detected, BugBot attempts to fix them and re-run, up to 5 times.
6. **Feedback:** You get clear output, error explanations, and fixed code.

---

## 📄 Example Usage

> **Prompt:**  
> "Write a function that takes a string and returns it reversed."

BugBot will:
- Generate the function
- Ask for your input string
- Run the code and show the result
- Fix any errors automatically

