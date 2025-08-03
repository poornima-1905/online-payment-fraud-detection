import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import numpy as np

# 1. Load data
df = pd.read_csv('creditcard.csv')

# 2. Create logic-based features
df['Hour'] = (df['Time'] // 3600) % 24
df['AmountLog'] = np.log1p(df['Amount'])
df['LateHour'] = df['Hour'].apply(lambda x: 1 if x <= 6 else 0)
df['AmountIsHigh'] = df['Amount'].apply(lambda x: 1 if x > 2000 else 0)

# 3. Select features and target
features = ['Hour', 'AmountLog', 'LateHour', 'AmountIsHigh']
X = df[features]
y = df['Class']

# 4. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# 5. Train model
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# 6. Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred, digits=4))

# 7. Save model
joblib.dump(model, 'supervise_model.pkl')
print("✅ Model saved as supervise_model.pkl")
