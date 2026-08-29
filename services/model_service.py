class ModelService:
    def __init__(self):
        self.models=[
            {"name":"Churn Classifier","type":"Classification","metric":.94,"status":"approved","owner":"risk-team"},
            {"name":"Demand Forecaster","type":"Regression","metric":.91,"status":"staging","owner":"sales-ops"},
            {"name":"Risk Scorer","type":"Classification","metric":.93,"status":"approved","owner":"fraud-ops"},
        ]

    def summary(self):
        return {"registry_size": len(self.models), "models": self.models, "best_model": max(self.models, key=lambda item: item["metric"])["name"]}

    def list_models(self):
        return {
            "models": self.models,
            "summary": {
                "registry_size": len(self.models),
                "best_model": max(self.models, key=lambda item: item["metric"])["name"],
                "average_metric": round(sum(item["metric"] for item in self.models) / len(self.models), 3),
            },
        }

    def train(self, name, task):
        metric = .91 if task.lower() == "regression" else .94
        item = {"name": name, "type": task, "metric": metric, "status": "trained", "owner": "ml-platform"}
        self.models.append(item)
        return item
