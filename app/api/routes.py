from fastapi import APIRouter
from app.ml.model import predict
from app.ml.anomaly_detector import detect_anomaly

router = APIRouter()

@router.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }

@router.post("/predict")
async def prediction(data: dict):

    prediction_result = predict(data)

    anomaly = detect_anomaly(prediction_result)

    return {
        "prediction": prediction_result,
        "anomaly_detected": anomaly
    }