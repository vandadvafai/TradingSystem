import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Get the base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load historical stock data
data_file = os.path.join(BASE_DIR, 'data/processed/output.csv')
data = pd.read_csv(data_file)

# Feature Engineering: Creating target variable (1 if price increased, 0 otherwise)
data['Target'] = (data['Close'].shift(-1) > data['Close']).astype(int)

# Selecting features
features = ['Open', 'High', 'Low', 'Close', 'Volume']
X = data[features]
y = data['Target']

# Handle missing values
dropna_indices = data.dropna().index
X, y = X.loc[dropna_indices], y.loc[dropna_indices]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=False)

# Standardizing features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Evaluate the model
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy:.2f}')

# Save model and scaler
joblib.dump(model, os.path.join(BASE_DIR, 'stock_price_predictor.pkl'))
joblib.dump(scaler, os.path.join(BASE_DIR, 'scaler.pkl'))

def predict_next_day(prices_df):
    """Loads the trained model and scaler, then predicts the next day's movement."""
    model = joblib.load(os.path.join(BASE_DIR, "stock_price_predictor.pkl"))
    scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))

    features = ['Open', 'High', 'Low', 'Close', 'Volume']
    X = prices_df[features].iloc[-1:].values  # Get the latest row for prediction

    X_scaled = scaler.transform(X)
    prediction = model.predict(X_scaled)[0]

    return "Price will rise" if prediction == 1 else "Price will fall"
