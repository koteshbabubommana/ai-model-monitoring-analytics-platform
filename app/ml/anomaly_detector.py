def detect_anomaly(prediction_score: float, latency_ms: float = 0) -> bool:
    if prediction_score >= 0.90:
        return True

    if prediction_score <= 0.10:
        return True

    if latency_ms > 500:
        return True

    return False