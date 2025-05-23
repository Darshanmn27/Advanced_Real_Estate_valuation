import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
import os

# Load the data
df = pd.read_csv("real_estate_data.csv")

# Drop missing values (or handle them differently if needed)
df.dropna(inplace=True)

# --- Step 1: Encode categorical variables ---
df = pd.get_dummies(df, columns=['location'], drop_first=True)

# --- Step 2: Define features and target ---
target_column = 'price'

if target_column not in df.columns:
    raise ValueError(f"Target column '{target_column}' not found in dataset.")

# Define target variable
y = df[target_column]

# Define feature variables
X = df[['size', 'rooms', 'location_Suburb', 'location_Uptown']]

# --- Step 3: Split data ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Step 4: Train model ---
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# --- Step 5: Evaluate model ---
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Model trained successfully. MSE: {mse:.2f}")

# --- Step 6: Save model ---
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/Random_Forest.pkl")
print("✅ Model saved at: models/Random_Forest.pkl")
