import time
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models import Base, PredictionLog
from app.database.connection import engine
from app.ml.model import predict
from app.ml.anomaly_detector import detect_anomaly
from app.analytics.metrics_service import calculate_summary

Base.metadata.create_all(bind=engine)

router = APIRouter()


class PredictionRequest(BaseModel):
    sample_input: float
    model_name: str = "customer-risk-model"


@router.get("/health")
async def health_check():
    return {"status": "healthy"}


@router.post("/predict")
async def prediction(request: PredictionRequest, db: Session = Depends(get_db)):
    start_time = time.time()

    prediction_result = predict({
        "sample_input": request.sample_input,
        "model_name": request.model_name
    })

    latency_ms = round((time.time() - start_time) * 1000, 2)
    prediction_score = prediction_result["model_prediction_score"]
    anomaly = detect_anomaly(prediction_score, latency_ms)

    log = PredictionLog(
        model_name=request.model_name,
        model_version=prediction_result["model_version"],
        input_value=request.sample_input,
        prediction_score=prediction_score,
        anomaly_detected=anomaly,
        latency_ms=latency_ms
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    return {
        "request_id": log.id,
        "prediction": prediction_result,
        "anomaly_detected": anomaly,
        "latency_ms": latency_ms,
        "stored_in_database": True
    }


@router.get("/analytics/summary")
async def analytics_summary(db: Session = Depends(get_db)):
    logs = db.query(PredictionLog).all()
    return calculate_summary(logs)


@router.get("/predictions")
async def get_predictions(db: Session = Depends(get_db)):
    logs = db.query(PredictionLog).order_by(PredictionLog.id.desc()).limit(10).all()

    return [
        {
            "id": log.id,
            "model_name": log.model_name,
            "prediction_score": log.prediction_score,
            "anomaly_detected": log.anomaly_detected,
            "latency_ms": log.latency_ms,
            "created_at": log.created_at
        }
        for log in logs
    ]


@router.get("/")
async def root():
    return {
        "message": "AI Model Monitoring Platform Running"
    }