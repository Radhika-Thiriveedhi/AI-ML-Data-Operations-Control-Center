from flask import Blueprint, jsonify, render_template, request
from services.pipeline_service import PipelineService
from services.model_service import ModelService
from services.monitoring_service import MonitoringService

bp = Blueprint("main", __name__)
pipeline = PipelineService()
models = ModelService()
monitor = MonitoringService()


@bp.get("/")
def home():
    return render_template("index.html")


@bp.get("/api/health")
def health():
    return jsonify({"status": "ok", "service": "ai-ml-data-operations-control-center"})


@bp.get("/api/overview")
def overview():
    return jsonify({"pipeline": pipeline.summary(), "models": models.summary(), "monitoring": monitor.summary()})


@bp.post("/api/pipeline/run")
def run_pipeline():
    source = (request.get_json(silent=True) or {}).get("source", "sample dataset")
    source = (source or "").strip()
    if not source:
        return jsonify({"error": "source is required"}), 400
    return jsonify(pipeline.run(source))


@bp.post("/api/models/train")
def train_model():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "Production Model").strip() or "Production Model"
    task = (data.get("task") or "Classification").strip()
    if task not in {"Classification", "Regression"}:
        return jsonify({"error": "task must be one of: Classification, Regression"}), 400
    return jsonify(models.train(name, task))


@bp.post("/api/monitoring/check")
def check():
    return jsonify(monitor.check())


main_bp = bp
