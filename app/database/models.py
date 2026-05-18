from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class PredictionLog(Base):
    __tablename__ = "prediction_logs"

    id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String, default="customer-risk-model")
    model_version = Column(String, default="v1.0")
    input_value = Column(Float)
    prediction_score = Column(Float)
    anomaly_detected = Column(Boolean)
    latency_ms = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)