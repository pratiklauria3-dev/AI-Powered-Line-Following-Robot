import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("ir_data_v3.csv")

# Clean action column
df["Action"] = df["Action"].str.strip()

# Encode labels
mapping = {"Forward":0, "Left":1, "Right":2}
df["Action"] = df["Action"].map(mapping)

X = df[["S1","S2","S3","S4","S5"]]
y = df["Action"]

model = RandomForestClassifier(
    n_estimators=250,
    max_depth=10,
    random_state=42
)

model.fit(X, y)

joblib.dump(model, "line_model_v3.pkl")

print("Model trained and saved as line_model_v3.pkl")