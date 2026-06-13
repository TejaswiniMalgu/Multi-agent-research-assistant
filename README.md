# 🔬 Multi-Agent Research Assistant
Live here: https://research-assistant-travily-mistral.streamlit.app/

An AI-powered research pipeline that autonomously searches the web, reads sources, writes structured reports, and critiques its own output — all in one run.

Built with **Tavily**, **Mistral AI**, **LangChain**, and **Streamlit**.

---

## ✨ Features

- **4-stage autonomous pipeline** — Search → Read → Write → Critique
- **Multi-agent architecture** — separate agents for search and deep reading
- **Streamlit UI** with live pipeline progress tracking
- **CLI support** — runs fully in terminal without any UI
- **Downloadable reports** — export as `.md` files
- **Deployable** — one-click deploy to Streamlit Cloud

---

## 🏗️ Architecture

```
User Input (Topic)
       │
       ▼
┌─────────────────┐
│  Search Agent   │  ← web_search tool (Tavily API)
│  (Mistral 7B)   │    Returns titles, URLs, snippets
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Reader Agent   │  ← scrape_url tool (BeautifulSoup)
│  (Mistral 7B)   │    Deep-reads the most relevant URL
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Writer Chain   │  ← LCEL chain (prompt → LLM → parser)
│  (Mistral 7B)   │    Produces structured research report
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Critic Chain   │  ← LCEL chain
│  (Mistral 7B)   │    Scores and reviews the report
└─────────────────┘
```

---

## 📁 Project Structure

```
Multi-Agent-Research-Assistant/
├── app.py              # Streamlit UI
├── agents.py           # Agent & chain definitions
├── pipeline.py         # CLI pipeline runner
├── tools.py            # web_search & scrape_url tools
├── requirements.txt    # Python dependencies
├── runtime.txt         # Python version pin (3.11)
└── .env                # API keys (not committed)
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-research-assistant.git
cd multi-agent-research-assistant
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root:

```env
TAVILY_API_KEY=your_tavily_api_key_here
MISTRAL_API_KEY=your_mistral_api_key_here
```

Get your keys:
- Tavily — [app.tavily.com](https://app.tavily.com)
- Mistral — [console.mistral.ai](https://console.mistral.ai)

---

## 🖥️ Running the App

### Streamlit UI (recommended)

```bash
# Using venv Python directly (most reliable)
.venv\Scripts\python.exe -m streamlit run app.py   # Windows
python -m streamlit run app.py                      # macOS / Linux
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

### Command Line (no UI)

```bash
python pipeline.py
```

Enter a topic when prompted. Output prints directly to terminal.

---

## ☁️ Deploy to Streamlit Cloud

1. Push your project to a **public GitHub repository**
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**
3. Select your repo → branch `main` → main file `app.py`
4. Under **Advanced settings**, set Python version to `3.11`
5. Click **Deploy**
6. After deploy, go to **Settings → Secrets** and add:

```toml
TAVILY_API_KEY = "your_tavily_key"
MISTRAL_API_KEY = "your_mistral_key"
```

Your app will be live at a public URL instantly.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| LLM | Mistral AI (`open-mistral-7b`) |
| Chains | LangChain LCEL |
| Web Search | Tavily API |
| Web Scraping | BeautifulSoup4 + Requests |
| UI | Streamlit |
| Deployment | Streamlit Cloud |

---

## 📄 Sample Output

**Input:** `Quantum computing applications in drug discovery`

**Output:**
- Structured report with Introduction, Key Findings, Conclusion, and Sources
- Critic score (e.g. `8/10`) with strengths and areas to improve
- Downloadable `.md` file

---

## 🔒 Environment Variables

| Variable | Description |
|---|---|
| `TAVILY_API_KEY` | Tavily search API key |
| `MISTRAL_API_KEY` | Mistral AI API key |

Never commit your `.env` file. It is listed in `.gitignore`.

---

## 📌 .gitignore

Make sure your `.gitignore` includes:

```
.env
.venv/
__pycache__/
*.pyc
```

---

## 👩‍💻 Author

**Tejaswini Malgu**  
B.Tech CSE (Data Science) · CVR College of Engineering  
[GitHub](https://github.com/YOUR_USERNAME) · [LinkedIn](https://linkedin.com/in/YOUR_PROFILE)
