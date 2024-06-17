import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

# Load data
data = pd.read_csv('../data/creditcard.csv')

# Perform data preprocessing
# Splitting data into features (X) and target (y)
X = data.drop(columns=['Class'])
y = data['Class']

# Handle class imbalance using SMOTE
smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X, y)

# Scale features
scaler = StandardScaler()
X_res = scaler.fit_transform(X_res)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42, stratify=y_res)

# Save preprocessed data
pd.DataFrame(X_train).to_csv('../data/X_train.csv', index=False)
pd.DataFrame(X_test).to_csv('../data/X_test.csv', index=False)
pd.DataFrame(y_train).to_csv('../data/y_train.csv', index=False)
pd.DataFrame(y_test).to_csv('../data/y_test.csv', index=False)
