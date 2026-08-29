# ML & Data Operations Control Center

A production-style AI/ML and data application covering data ingestion, preprocessing, feature engineering concepts, model training, registry workflows and operational monitoring. It uses Flask routers and interactive buttons and requires no database connection.

## Features
- Data pipeline execution dashboard
- Schema and preprocessing workflow
- Feature engineering and quality-control architecture
- Model training and registry simulation
- Drift, latency, freshness and health monitoring
- Stateless REST APIs
- Responsive browser UI
- Automated tests and CI

## Install
`python -m venv .venv`
Windows PowerShell: `.venv\Scripts\Activate.ps1`
`pip install -r requirements.txt`

## Build
`python -m compileall app services run.py`

## Run
`python run.py`
Open `http://127.0.0.1:5000`

## Test
`python -m pytest`

## Structure
`app/` routers and application factory; `services/` ML/data services; `templates/` UI; `static/` browser assets; `tests/` CI tests.
