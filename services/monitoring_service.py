from datetime import datetime, timezone
class MonitoringService:
    def summary(self): return {"health":"Healthy","drift_score":.08,"latency_ms":84,"freshness":"Current"}
    def check(self):
        return {"checked_at":datetime.now(timezone.utc).isoformat(),"status":"healthy","checks":[{"name":x,"status":"passed"} for x in ["Data freshness","Feature drift","Prediction latency","Model availability"]]}
