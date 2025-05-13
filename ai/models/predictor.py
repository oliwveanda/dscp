import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

class AirQualityPredictor:
    def __init__(self):
        self.model = None

    def train_model(self, data_path):
        data = pd.read_csv(data_path)
        
        # Example: Using temperature and humidity as features for PM2.5 prediction
        X = data[['temperature', 'humidity']]
        y = data['PM2.5']

        model = LinearRegression()
        model.fit(X, y)

        self.model = model

        os.makedirs('ai/models', exist_ok=True)
        joblib.dump(model, 'ai/models/air_quality_model.pkl')

    def predict(self, temperature, humidity):
        if self.model is None:
            self.model = joblib.load('ai/models/air_quality_model.pkl')
        
        prediction = self.model.predict([[temperature, humidity]])
        return prediction[0]
