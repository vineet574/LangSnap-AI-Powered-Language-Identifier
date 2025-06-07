import joblib

def predict(text):
    model = joblib.load('models/language_model.pkl')
    prediction = model.predict([text])[0]
    proba = model.predict_proba([text])[0]
    confidence = max(proba) * 100
    return prediction, confidence
