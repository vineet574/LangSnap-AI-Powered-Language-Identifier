import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

def train():
    df = pd.read_csv('data/language_dataset.csv')
    X = df['text']
    y = df['language']

    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X, y)

    joblib.dump(model, 'models/language_model.pkl')
    print("Model trained and saved!")

if __name__ == "__main__":
    train()
