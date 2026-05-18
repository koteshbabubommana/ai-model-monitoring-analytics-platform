import random

def predict(data):

    prediction_score = round(random.uniform(0.1, 0.99), 4)

    return {
        "model_prediction_score": prediction_score,
        "model_version": "v1.0"
    }