from flask import Blueprint, jsonify, render_template, request
from services.pipeline_service import PipelineService
from services.model_service import ModelService
from services.monitoring_service import MonitoringService
bp = Blueprint("main", __name__)
pipeline = PipelineService()
models = ModelService()
monitor = MonitoringService()

@bp.get("/")
def home(): return render_template("index.html")

@bp.get("/api/overview")
def overview():
    return jsonify({"pipeline": pipeline.summary(), "models": models.summary(), "monitoring": monitor.summary()})

@bp.post("/api/pipeline/run")
def run_pipeline():
    return jsonify(pipeline.run((request.get_json(silent=True) or {}).get("source", "sample dataset")))

@bp.post("/api/models/train")
def train_model():
    data = request.get_json(silent=True) or {}
    return jsonify(models.train(data.get("name", "Production Model"), data.get("task", "Classification")))

@bp.post("/api/monitoring/check")
def check(): return jsonify(monitor.check())

main_bp = bp
