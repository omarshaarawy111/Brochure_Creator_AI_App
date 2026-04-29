#  Brochure Creator AI App

A Streamlit-based web application that automatically generates comprehensive company brochures by analyzing a given website and its relevant sub-pages using OpenAI's LLMs.

## 📖 What It Does

This project automatically:
1. **Validates** user input through an interactive chat interface.
2. **Scrapes** the provided URL and uses an LLM to identify relevant internal links (e.g., About Us, Careers, Contact).
3. **Fetches** the content from the main page and all the identified relevant links.
4. **Generates** a high-quality, Markdown-formatted company brochure streamed to the UI in real-time.
5. **Handles** out-of-scope questions with a conversational fallback model.

## 🎯 Key Features

- ✅ **Streamlit Chat UI:** A sleek, conversational interface with text streaming.
- ✅ **Multi-Step AI Pipeline:** Intelligently finds relevant links before generating content.
- ✅ **Real-Time Status Updates:** See exactly what the AI is doing (finding links, scraping, etc.) via UI status containers.
- ✅ **Audio Notifications:** Plays a ping sound when a prompt is submitted.
- ✅ **Custom Error Handling:** Verifies valid API keys and gracefully fields non-URL chat messages.

## 🛠️ Technologies Used

- **Python 3.9+**
- **Streamlit** — For the interactive web interface.
- **OpenAI Python SDK** — For intelligent link filtering and content generation.
- **BeautifulSoup4 / requests** — For scraping and parsing HTML content.
- **python-dotenv** — For managing environment variables securely.

## 📋 Prerequisites

1. Python 3.9 or higher.
2. An OpenAI API key (ensure it is a valid project key starting with `sk-proj-`).

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Brochure_Creator_AI_App
   ```

2. **Install dependencies**
   It's recommended to use a virtual environment.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY="sk-proj-..."
   ```
   > ⚠️ **Never commit your `.env` file to GitHub!**

## 💡 How to Use

Run the application using Streamlit:

```bash
streamlit run app.py
```

You can also specify a different model:
```bash
python src/main.py "https://www.deeplearning.ai/" --model gpt-3.5-turbo
```
