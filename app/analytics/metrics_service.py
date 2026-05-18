def calculate_summary(prediction_logs):
    total_predictions = len(prediction_logs)

    if total_predictions == 0:
        return {
            "total_predictions": 0,
            "average_score": 0,
            "anomaly_count": 0
        }

    average_score = sum(log.prediction_score for log in prediction_logs) / total_predictions
    anomaly_count = sum(1 for log in prediction_logs if log.anomaly_detected)

    return {
        "total_predictions": total_predictions,
        "average_score": round(average_score, 4),
        "anomaly_count": anomaly_count
    }