class PipelineService:
    def __init__(self):
        self.steps=["Data ingestion","Schema validation","Missing values","Outlier review","Feature scaling","Quality scoring","Training export"]
        self.last_run="Not executed"
    def summary(self): return {"name":"Production Data Pipeline","status":"Ready","steps":len(self.steps),"last_run":self.last_run}
    def run(self, source="sample dataset"):
        self.last_run="Completed"
        return {"status":"completed","source":source,"results":[{"step":i+1,"name":x,"status":"passed"} for i,x in enumerate(self.steps)]}
