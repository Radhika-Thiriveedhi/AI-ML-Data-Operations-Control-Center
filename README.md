# ML & Data Operations Control Center

A production-style AI/ML and data application covering data ingestion, preprocessing, feature engineering concepts, model training, registry workflows, and operational monitoring. It uses Flask routes and a lightweight browser UI and does not require a database.

## Highlights
- Data pipeline execution dashboard
- Schema and preprocessing workflow orchestration
- Feature engineering and quality-control architecture
- Model training and registry simulation
- Drift, latency, freshness, and health monitoring
- Stateless REST APIs
- Responsive browser UI
- Automated tests and CI-friendly validation

## Quick start

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py
```

Open http://127.0.0.1:5000

## Useful commands

```bash
python -m pytest
python -m compileall app services run.py
```

## Docker

```bash
docker build -t ml-ops-control-center .
docker run -p 5000:5000 ml-ops-control-center
```

## Project structure
- app/: Flask app and route definitions
- services/: ML and data operations service logic
- templates/: browser UI
- static/: frontend assets
- tests/: regression tests

## Operational endpoints
- GET /api/health
- GET /api/overview
- GET /api/models
- POST /api/pipeline/run
- POST /api/models/train
- GET /api/monitoring/metrics
- POST /api/monitoring/check
