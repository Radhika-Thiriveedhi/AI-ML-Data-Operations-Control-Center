from app import create_app

def client(): return create_app().test_client()


def test_home():
    assert client().get("/").status_code == 200


def test_overview():
    assert client().get("/api/overview").json["models"]["registry_size"] >= 3


def test_health_endpoint():
    resp = client().get("/api/health")
    assert resp.status_code == 200
    assert resp.json["status"] == "ok"


def test_pipeline_rejects_blank_source():
    resp = client().post("/api/pipeline/run", json={"source": "   "})
    assert resp.status_code == 400
    assert "source" in resp.json["error"]


def test_pipeline():
    assert len(client().post("/api/pipeline/run", json={"source": "x"}).json["results"]) == 7


def test_training_rejects_invalid_task():
    resp = client().post("/api/models/train", json={"name": "x", "task": "Invalid"})
    assert resp.status_code == 400
    assert "task" in resp.json["error"]


def test_training():
    assert client().post("/api/models/train", json={"name": "x", "task": "Classification"}).json["status"] == "trained"


def test_monitoring():
    assert client().post("/api/monitoring/check").json["status"] == "healthy"
