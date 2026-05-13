# Business AI Assistant

A full-stack AI-powered business intelligence tool that analyses business reports and returns structured summaries, key insights, and actionable recommendations — powered by OpenAI GPT.

---

## Features

- Paste any business report, financial data, or operational text and get instant AI analysis
- Three structured outputs: Summary, Key Insights, and Recommendations
- Analysis history stored locally in the browser — expand, review, or delete past analyses
- Settings page to configure backend URL, AI model, and response language
- Clean, professional dark UI built with Vue 3

---

## Tech Stack

| Layer    | Technology                        |
|----------|-----------------------------------|
| Frontend | Vue 3, Vue Router, Vite, Axios    |
| Backend  | Python, Flask, Flask-CORS         |
| AI       | OpenAI GPT (gpt-3.5-turbo / gpt-4)|

---

## Project Structure

```
business-ai-assistant/
├── backend/
│   ├── app.py            # Flask API server
│   ├── ai_service.py     # OpenAI integration
│   ├── requirements.txt  # Python dependencies
│   └── .env              # API key (not committed)
└── frontend/
    ├── src/
    │   ├── views/
    │   │   ├── AnalysisView.vue   # Main analysis page
    │   │   ├── HistoryView.vue    # Past analyses
    │   │   └── SettingsView.vue   # Configuration
    │   ├── router/index.js
    │   ├── App.vue
    │   └── main.js
    ├── index.html
    └── package.json
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 20+
- An OpenAI API key — get one at https://platform.openai.com/api-keys

---

### 1. Clone the repository

```bash
git clone https://github.com/dara283/business-ai-assistant.git
cd business-ai-assistant
```

---

### 2. Backend Setup

```bash
cd backend
python -m pip install -r requirements.txt
```

Create a `.env` file in the `backend/` folder:

```
OPENAI_API_KEY=your_openai_api_key_here
```

Start the backend:

```bash
python app.py
```

The API will run on `http://127.0.0.1:5000`.

---

### 3. Frontend Setup

```bash
cd frontend
npm install --legacy-peer-deps
npm run dev
```

The app will run on `http://localhost:5173`.

---

## API Reference

### `POST /analyse`

Analyses the provided business text and returns structured AI output.

**Request body:**
```json
{
  "text": "Your business report or data here..."
}
```

**Response:**
```json
{
  "summary": "...",
  "insights": "...",
  "recommendations": "..."
}
```

---

## Test Data

Paste the following into the analysis input to test the system:

```
Q3 2024 Performance Report — Acme Retail Group

Total Revenue: $4.2M (up 18% YoY)
Gross Margin: 34% (down from 38% in Q2)
Operating Expenses: $1.1M (up 22% due to new warehouse lease)
Net Profit: $320,000

Top Performing Categories:
- Electronics: $1.6M (+31%)
- Home & Garden: $890K (+12%)
- Apparel: $540K (-8%)

Customer Metrics:
- New customers acquired: 3,420
- Returning customer rate: 61%
- Average order value: $127 (up from $109)
- Cart abandonment rate: 47%

Regional Breakdown:
- North: $1.8M (+24%)
- South: $1.1M (+9%)
- West: $820K (+14%)
- East: $480K (-3%)

Challenges:
- Supply chain delays impacted apparel restocking
- Rising logistics costs reduced gross margin
- East region underperforming due to increased local competition
```

---

## Environment Variables

| Variable         | Description                        |
|------------------|------------------------------------|
| `OPENAI_API_KEY` | Your OpenAI secret key             |

> The `.env` file is excluded from version control. Never commit your API key.

---

## License

MIT
