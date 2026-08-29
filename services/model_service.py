class ModelService:
    def __init__(self):
        self.models=[{"name":"Churn Classifier","type":"Classification","metric":.94},{"name":"Demand Forecaster","type":"Regression","metric":.91},{"name":"Risk Scorer","type":"Classification","metric":.93}]
    def summary(self): return {"registry_size":len(self.models),"models":self.models}
    def train(self,name,task):
        metric=.91 if task.lower()=="regression" else .94
        item={"name":name,"type":task,"metric":metric,"status":"trained"}
        self.models.append(item); return item
