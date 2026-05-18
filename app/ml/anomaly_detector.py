def detect_anomaly(prediction):

    score = prediction["model_prediction_score"]

    if score > 0.90:
        return True

    return False