import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer  # type: ignore
from sklearn.preprocessing import OneHotEncoder  # type: ignore
from sklearn.model_selection import train_test_split  # type: ignore
from sklearn.pipeline import Pipeline  # type: ignore
from sklearn.linear_model import LinearRegression  # type: ignore
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score  # type: ignore
from sklearn.ensemble import RandomForestRegressor  # type: ignore

# --------------------------------
# 1. Load dataset
# --------------------------------

df = pd.read_csv("dataset/Dataset.csv")


# --------------------------------
# 2. Remove duplicates
# --------------------------------

df = df.drop_duplicates()


# --------------------------------
# 3. Handle missing values
# --------------------------------

df["Teacher_Quality"] = df["Teacher_Quality"].fillna(
    df["Teacher_Quality"].mode()[0]
)

df["Parental_Education_Level"] = df["Parental_Education_Level"].fillna(
    df["Parental_Education_Level"].mode()[0]
)

df["Distance_from_Home"] = df["Distance_from_Home"].fillna(
    df["Distance_from_Home"].mode()[0]
)


# --------------------------------
# 4. Separate X and y
# --------------------------------

X = df.drop("Exam_Score", axis=1)

y = df["Exam_Score"]


# --------------------------------
# 5. Find categorical columns
# --------------------------------

categorical_columns = X.select_dtypes(
    include="object"
).columns


# --------------------------------
# 6. Create preprocessor
# --------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        )
    ],
    remainder="passthrough"
)


# --------------------------------
# 7. Train-Test Split
# --------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


print("\nTrain-Test Split:")
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)


# --------------------------------
# 8. Create Linear Regression model
# --------------------------------

linear_model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", LinearRegression())
    ]
)


# --------------------------------
# 9. Train model
# --------------------------------

linear_model.fit(X_train, y_train)

print("\nLinear Regression model trained successfully.")


# --------------------------------
# 10. Make predictions
# --------------------------------

y_pred = linear_model.predict(X_test)


print("\nFirst 10 Predictions:")

for actual, predicted in zip(
    y_test.head(10),
    y_pred[:10]
):
    print(
        f"Actual: {actual}, Predicted: {predicted:.2f}"
    )


# --------------------------------
# Evaluate the model
# --------------------------------


mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE:", round(mae, 2))
print("MSE:", round(mse, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 4))



#--------------------------------
# Create Random Forest pipeline
#-------------------------------


rf_model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", RandomForestRegressor(
            n_estimators=100,
            random_state=42
        ))
    ]
)

# Train Random Forest
rf_model.fit(X_train, y_train)

print("\nRandom Forest model trained successfully.")

# Make predictions
rf_pred = rf_model.predict(X_test)


# Evaluate Random Forest

rf_mae = mean_absolute_error(y_test, rf_pred)

rf_mse = mean_squared_error(y_test, rf_pred)

rf_rmse = np.sqrt(rf_mse)

rf_r2 = r2_score(y_test, rf_pred)

print("\nRandom Forest Evaluation:")
print("MAE:", round(rf_mae, 2))
print("MSE:", round(rf_mse, 2))
print("RMSE:", round(rf_rmse, 2))
print("R2 Score:", round(rf_r2, 4))


import joblib  # type: ignore[import-not-found]

# Save the best model
joblib.dump(linear_model, "model/student_model.pkl")

print("\nLinear Regression model saved successfully.")