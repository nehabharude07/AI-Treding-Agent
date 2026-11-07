
# 🚀 AI Trading Agent

An interactive AI-powered trading analysis web application built with FastAPI, Python, HTML, CSS, and JavaScript. It accepts portfolio and market parameters and displays the trading signal and performance metrics returned by the backend.

## ✨ Features

- Interactive dark neon and glassmorphism UI
- Portfolio value and trade size inputs
- OHLCV market data inputs (Open, High, Low, Close, Volume)
- Backend integration through a REST API
- Trading signal display (BUY, SELL, or HOLD, depending on model output)
- Total return / profit display
- Sharpe Ratio display when available from the backend
- Responsive layout for desktop and mobile
- Loading indicator and error handling

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI
- **Frontend:** HTML, CSS, JavaScript
- **API Server:** Uvicorn
- **Template Engine:** Jinja2
- **Model:** Trained trading model, if configured

## 📁 Project Structure

```text
AI-Trading-Agent/
├── app/
│   └── main.py
├── frontend/
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── css/
│           └── style.css
├── models/
│   └── trading_model.pkl
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

The exact structure may differ depending on your local project files.

## ⚙️ Prerequisites

- Python 3.11 or a compatible version
- pip
- Git
- A trained model file if required by the backend

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/nehabharude07/AI-Trading-Agent.git
cd AI-Trading-Agent
```

Replace the repository URL with your actual GitHub repository URL if it differs.

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

If `requirements.txt` does not exist, create it using the dependencies actually used by your project.

### 4. Configure environment variables

Create a local `.env` file using `.env.example` as a template.

Do not commit `.env` or put passwords, API keys, or other secrets in GitHub.

### 5. Configure the model

Place the trained model at the path expected by your backend, such as:

```text
models/trading_model.pkl
```

The model file must exist and be compatible with the loading and prediction code in `app/main.py`.

### 6. Start the application

```bash
python -m uvicorn app.main:app --reload
```

Open the application:

http://127.0.0.1:8000

FastAPI interactive API documentation, when enabled:

http://127.0.0.1:8000/docs

## 📊 How to Use

1. Open the application in your browser.
2. Enter your portfolio value and trade size.
3. Enter the Open, High, Low, Close, and Volume values.
4. Click **Run Agent**.
5. Review the trading signal and available performance metrics.

The frontend sends a POST request to `/run-agent`. The backend must implement the endpoint and return the expected JSON fields.

## 📈 Performance Metrics

- **Signal:** Trading recommendation returned by the model.
- **Total Return:** Profit or return value supplied by the backend.
- **Sharpe Ratio:** Risk-adjusted return metric, displayed when provided by the backend. It may show N/A when the backend does not calculate or return it.

## 🔒 Security and Disclaimer

- Never commit `.env`, credentials, access tokens, or private keys.
- Only load trusted model files.
- This project is for educational and research purposes.
- Trading signals are not guaranteed to be profitable and should not be treated as financial advice.
- Validate model outputs and test the application before using it with real money.

## 👩‍💻 Author

Neha Bharule

GitHub: https://github.com/nehabharude07
