import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
import joblib

# Load preprocessed data
X_train = pd.read_csv('../data/X_train.csv')
X_test = pd.read_csv('../data/X_test.csv')
y_train = pd.read_csv('../data/y_train.csv')
y_test = pd.read_csv('../data/y_test.csv')

# Start an MLflow run
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.start_run()

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train.values.ravel())

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

# Log metrics and model with MLflow
mlflow.log_param("n_estimators", 100)
mlflow.log_metric('accuracy', accuracy)
mlflow.log_metric('precision', precision)
mlflow.log_metric('recall', recall)
mlflow.sklearn.log_model(model, "random_forest_model")

# End the MLflow run
mlflow.end_run()

# Save the trained model using joblib
joblib.dump(model, '../models/model.joblib')



