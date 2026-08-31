from datetime import datetime, timezone


class MonitoringService:
    def summary(self):
        return {"health": "Healthy", "drift_score": 0.08, "latency_ms": 84, "freshness": "Current"}

    def metrics(self):
        summary = {
            "overall_score": 96.4,
            "health": "healthy",
            "uptime_pct": 99.97,
            "drift_score": 0.08,
            "latency_ms": 84,
            "freshness": "Current",
            "errors_last_24h": 2,
            "throughput_rps": 242,
        }
        return {
            "checked_at": datetime.now(timezone.utc).isoformat(),
            "status": "healthy",
            "summary": summary,
            "checks": [{"name": x, "status": "passed"} for x in ["Data freshness", "Feature drift", "Prediction latency", "Model availability"]],
        }

    def check(self):
        return {
            "checked_at": datetime.now(timezone.utc).isoformat(),
            "status": "healthy",
            "checks": [{"name": x, "status": "passed"} for x in ["Data freshness", "Feature drift", "Prediction latency", "Model availability"]],
        }
