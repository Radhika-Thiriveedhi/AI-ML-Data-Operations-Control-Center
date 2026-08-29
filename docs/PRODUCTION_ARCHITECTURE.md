# Production Architecture

This application is a database-free ML operations control center.

The production service layer is organized around ingestion, preprocessing,
feature engineering, training, evaluation, registry, deployment, serving,
monitoring, governance, security, lineage, and reporting.

Each engine exposes deterministic methods so the UI and HTTP routers can
exercise workflows without external credentials or database connections.
The modules are intentionally separated so production implementations can
later be replaced with cloud queues, feature stores, model registries, or
real ML estimators without changing the browser interface.

Operational flow:
1. Ingest a source dataset.
2. Validate schema and data quality.
3. Apply preprocessing controls.
4. Construct and validate features.
5. Train and evaluate a model.
6. Register and release the model.
7. Serve predictions.
8. Monitor drift, latency, freshness, and quality.
9. Record lineage and operational events.
10. Produce an operations report.
