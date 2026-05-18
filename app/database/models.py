from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class PredictionLog(Base):
    __tablename__ = "prediction_logs"

    id = Column(Integer, primary_key=True, index=True)
    model_version = Column(String, default="v1.0")
    prediction_score = Column(Float)
    anomaly_detected = Column(Boolean)
    latency_ms = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)