import os
import pickle
import numpy as np
from flask import Flask, request, render_template

application = Flask(__name__)
app = application

# Get base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model and scaler using absolute path
scaler_path = os.path.join(BASE_DIR, 'Model', 'standardScalar.pkl')
model_path = os.path.join(BASE_DIR, 'Model', 'modelForPrediction.pkl')

scaler = pickle.load(open(scaler_path, "rb"))
model = pickle.load(open(model_path, "rb"))

# Homepage
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Prediction input form
@app.route('/predict')
def predict_input():
    return render_template('predict_input.html')

# Result handling
@app.route('/predict-result', methods=['POST'])
def predict_datapoint():
    if request.method == 'POST':
        try:
            # Get user input
            data = [
                int(request.form.get("Pregnancies")),
                float(request.form.get("Glucose")),
                float(request.form.get("BloodPressure")),
                float(request.form.get("SkinThickness")),
                float(request.form.get("Insulin")),
                float(request.form.get("BMI")),
                float(request.form.get("DiabetesPedigreeFunction")),
                float(request.form.get("Age"))
            ]

            # Preprocess and predict
            new_data = scaler.transform([data])
            prediction = model.predict(new_data)

            result = "Diabetic" if prediction[0] == 1 else "Non-Diabetic"

            return render_template("prediction_result.html", result=result)

        except Exception as e:
            return f"Error Occurred: {str(e)}"

    return render_template("predict_input.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)