# Installation Guide

## System Requirements

### Software

- Python 3.11+
- Node.js 20+
- npm
- Git
- Docker Desktop (Optional)

---

# Clone Repository

```bash
git clone <your-repository-url>

cd Enterprise-Financial-Intelligence-Platform
```

---

# Backend Setup

Navigate to backend:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI:

```bash
uvicorn app.main:app --reload
```

Backend will run at:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

# Frontend Setup

Navigate to frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start development server:

```bash
npm run dev
```

Frontend will run at:

```text
http://localhost:5173
```

---

# Running Tests

## Unit Tests

```bash
python -m pytest tests
```

---

## End-to-End Tests

```bash
python -m pytest tests/test_e2e_pipeline.py
```

---

# MLOps Setup

## MLflow

Launch MLflow UI:

```bash
mlflow ui
```

Default URL:

```text
http://localhost:5000
```

---

## DVC

Initialize DVC:

```bash
dvc init
```

Track dataset:

```bash
dvc add data/sample_financials.csv
```

---

# Docker Deployment

Build containers:

```bash
docker-compose build
```

Start containers:

```bash
docker-compose up
```

Stop containers:

```bash
docker-compose down
```

---

# Project Structure

```text
Enterprise Financial Intelligence Platform
│
├── backend
│   ├── app
│   ├── tests
│   └── requirements.txt
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
├── data
│   ├── sample_financials.csv
│   └── sample_forecast_data.csv
│
├── docs
│   ├── architecture.png
│   ├── API_DOCUMENTATION.md
│   ├── INSTALLATION.md
│   ├── BENCHMARKS.md
│   └── ROADMAP.md
│
└── docker-compose.yml
```

---

# Troubleshooting

## Port Already In Use

Frontend:

```bash
npm run dev
```

Vite automatically selects the next available port.

Backend:

```bash
uvicorn app.main:app --reload --port 8001
```

---

## Python Not Found

Use:

```bash
py
```

instead of:

```bash
python
```

on Windows.

---

## DVC Command Not Found

Use:

```bash
py -m dvc init
```

instead of:

```bash
dvc init
```

---

## Pytest Command Not Found

Use:

```bash
py -m pytest
```

instead of:

```bash
pytest
```

---

# Verification Checklist

After setup verify:

- Backend running
- Frontend running
- Swagger docs accessible
- Dashboard loads
- MLflow page loads
- DVC page loads
- Tests pass

If all checks pass, EFIP is ready for development and demonstration.