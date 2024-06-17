import joblib
from flask import Flask, request, jsonify
import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

app = Flask(__name__)

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), '../models/model.joblib')
model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame(data)
    
    # Load scaler and scale the data
    scaler = StandardScaler()
    df = scaler.fit_transform(df)
    
    # Predict using the model
    prediction = model.predict(df)
    
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
