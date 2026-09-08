# 🎓 Student Performance Prediction

A Machine Learning project that predicts student exam scores based on academic, behavioral, and demographic factors.

## 📌 Project Overview

The Student Performance Prediction system uses machine learning regression algorithms to predict a student's expected exam score.

The project includes:

- Data preprocessing
- Exploratory Data Analysis
- Feature encoding
- Train-test splitting
- Machine learning model training
- Model evaluation
- Model comparison
- Streamlit web application
- Performance recommendations

## 📊 Dataset

The project uses a student performance dataset obtained from Kaggle.

The dataset contains:

- 6,607 student records
- 20 columns

The target variable is:

`Exam_Score`

### Important Features

- Hours Studied
- Attendance
- Previous Scores
- Sleep Hours
- Tutoring Sessions
- Physical Activity
- Motivation Level
- Parental Involvement
- Access to Resources
- Teacher Quality
- Family Income
- Peer Influence
- Parental Education Level
- Distance From Home
- Gender

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

1. Checked dataset shape and information
2. Checked missing values
3. Removed duplicate rows
4. Handled missing categorical values using the mode
5. Separated features and target
6. Applied One-Hot Encoding to categorical variables
7. Split the dataset into training and testing sets

The dataset was divided using:

- 80% training data
- 20% testing data

## 🤖 Machine Learning Models

Two regression algorithms were tested:

### 1. Linear Regression

Performance:

- MAE: 0.45
- RMSE: 1.80
- R² Score: 0.7696

### 2. Random Forest Regressor

Performance:

- MAE: 1.09
- RMSE: 2.16
- R² Score: 0.6693

## 🏆 Model Selection

Linear Regression performed better than Random Forest based on MAE, RMSE and R² Score.

Therefore, Linear Regression was selected as the final prediction model.

## 📈 Exploratory Data Analysis

EDA was performed using:

- Matplotlib
- Seaborn
- Pandas

Visualizations included:

- Exam Score distribution
- Hours Studied vs Exam Score
- Attendance vs Exam Score
- Previous Scores vs Exam Score
- Motivation Level vs Exam Score
- Parental Involvement vs Exam Score
- Correlation heatmap

## 🌐 Streamlit Application

The trained model is integrated into a Streamlit web application.

Users can enter:

- Academic information
- Student information
- Behavioral information

The application provides:

- Predicted exam score
- Performance category
- Score visualization
- Personalized recommendations

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit
- Jupyter Notebook

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt