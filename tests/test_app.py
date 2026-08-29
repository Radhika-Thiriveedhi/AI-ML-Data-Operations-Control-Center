from app import create_app
def client(): return create_app().test_client()
def test_home(): assert client().get("/").status_code==200
def test_overview(): assert client().get("/api/overview").json["models"]["registry_size"]>=3
def test_pipeline(): assert len(client().post("/api/pipeline/run",json={"source":"x"}).json["results"])==7
def test_training(): assert client().post("/api/models/train",json={"name":"x","task":"Classification"}).json["status"]=="trained"
def test_monitoring(): assert client().post("/api/monitoring/check").json["status"]=="healthy"
