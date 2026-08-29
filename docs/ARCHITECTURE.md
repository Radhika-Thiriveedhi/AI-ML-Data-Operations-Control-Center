# Architecture

The system is intentionally stateless and database-free. Flask routers expose a small HTTP API and delegate work to service classes.

Data flow: ingestion -> validation -> preprocessing -> feature engineering -> model training -> registry -> monitoring.

The deterministic service layer can later be replaced with real ML algorithms or external storage without changing the UI contract.
