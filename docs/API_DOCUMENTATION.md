# API Documentation

## Base URL

http://localhost:8000

---

## Dashboard

### GET /dashboard

Returns executive KPI metrics.

Response:

```json
{
  "risk_score": 42,
  "forecast_score": 81,
  "portfolio_score": 76,
  "model_health": 91
}
```

---

## Company Analysis

### GET /company

Returns company financial analysis.

---

## Forecasting

### GET /forecast

Returns forecasting metrics and projections.

---

## Scenario Simulator

### POST /scenario

Request:

```json
{
  "revenue_change": 10,
  "cost_change": 5
}
```

Response:

```json
{
  "projected_profit": 1250000
}
```

---

## Monitoring

### GET /monitoring

Returns system monitoring information.

---

## System Status

### GET /system-status

Returns production readiness metrics.

---

## MLflow

### GET /mlflow-status

Returns experiment tracking information.

---

## DVC

### GET /dvc-status

Returns dataset versioning information.

---

## E2E

### GET /e2e-status

Returns pipeline validation status.

---

## Interactive Swagger Documentation

http://localhost:8000/docs