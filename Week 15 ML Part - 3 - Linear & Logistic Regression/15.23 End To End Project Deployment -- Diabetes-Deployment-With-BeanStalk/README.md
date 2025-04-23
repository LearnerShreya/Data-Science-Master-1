# 🩺 Diabetes Prediction Web App

A machine learning-based web application that predicts an individual's risk of diabetes based on user-provided health metrics. This project utilizes **Logistic Regression** for classification and is deployed with a responsive front-end using Flask and HTML/CSS.


## 🚀 Project Overview

This app empowers users to assess their risk of diabetes through a user-friendly interface. It takes in simple medical inputs and returns a real-time prediction using a trained machine learning model.

> **Model Used:** Logistic Regression (Scikit-learn)  
> **Deployment:** Flask (Python)  
> **Interface:** HTML + CSS (Responsive)  


## 🔧 Tech Stack

- **Language:** Python  
- **Backend Framework:** Flask  
- **Frontend:** HTML, CSS  
- **Environment:** Windows, VS Code, Jupyter Notebook  
- **Model Serialization:** Pickle  


## 📚 Libraries Used

- **Scikit-learn** – for model training (Logistic Regression)  
- **Pandas** – data handling  
- **NumPy** – numerical operations  
- **Matplotlib & Seaborn** – data visualization during development  


## 🧠 Features

- 🔍 **Accurate Predictions**: Trained Logistic Regression model for diabetes detection.
- 🎯 **Simple Inputs**: Users can easily input health-related parameters (e.g., BMI, age, glucose level).
- ⚡ **Instant Results**: Get predictions instantly with a single click.
- 🖥️ **Responsive UI**: Clean and modern front-end that works on all devices.
- 🔄 **Reusable Backend**: Easily replace or update the ML model using Pickle.


## 🧪 How It Works

1. The user accesses the web interface.
2. Inputs health parameters such as:
   - Pregnancies
   - Glucose
   - Blood Pressure
   - Skin Thickness
   - Insulin
   - BMI
   - Diabetes Pedigree Function
   - Age
3. The backend loads the pre-trained Logistic Regression model using Pickle.
4. The model processes the input and predicts whether the user is at risk for diabetes.
5. The result is displayed on the web page with appropriate styling and user experience.


<!-- ## 🛠️ Installation and Usage

```bash
# Clone the repository
git clone <project-link>

# Navigate to the directory
cd diabetes-prediction-app

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
``` -->

```
project/
├── application.py
├── Model/
│   ├── modelForPrediction.pkl
│   └── standardScalar.pkl
├── templates/
│   ├── welcome.html
│   ├── predict_input.html
│   └── prediction_result.html
├── requirements.txt
```

### 📝:
- `Notebook/`
- `Dataset/`
- `README.md`
- `.ebextensions/` (for AWS deploy)
- `data.json`

## 📈 Future Scope

- Integrate more ML models like Random Forest or XGBoost for comparison.
- Store user history and analytics dashboard.
- API integration for real-time health record data.
- Multilingual support and mobile-first design improvements.
