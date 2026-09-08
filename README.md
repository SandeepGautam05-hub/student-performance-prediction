# 🎓 Student Performance Prediction

A Machine Learning project that predicts student exam scores based on academic, behavioral, and demographic factors.

## 🌐 Live Demo

🚀 **Try the deployed application:**

👉 https://sandeep-student-performance-predictor-ml.streamlit.app/

## 💻 GitHub Repository

👉 https://github.com/SandeepGautam05-hub/student-performance-prediction

---

# 📌 Project Overview

The **Student Performance Prediction** system uses Machine Learning regression algorithms to predict a student's expected exam score.

The project analyzes academic, behavioral, and demographic factors that may be associated with student performance.

The project includes:

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Missing value handling
- Feature encoding
- Train-test splitting
- Machine learning model training
- Model evaluation
- Model comparison
- Model selection
- Model serialization
- Streamlit web application
- Personalized performance recommendations
- Cloud deployment

---

# 🎯 Project Objectives

The main objectives of this project are:

1. Analyze factors affecting student examination performance.
2. Perform data cleaning and preprocessing.
3. Explore relationships between different student factors and exam scores.
4. Train multiple machine learning regression models.
5. Compare model performance using evaluation metrics.
6. Select the best-performing model.
7. Build an interactive Streamlit application.
8. Deploy the application online for public access.

---

# 📊 Dataset

The project uses a **Student Performance Factors** dataset obtained from Kaggle.

### Dataset Information

- **Total Records:** 6,607
- **Total Columns:** 20
- **Target Variable:** `Exam_Score`

### Important Features

| Feature | Description |
|---|---|
| `Hours_Studied` | Number of hours spent studying |
| `Attendance` | Student attendance percentage |
| `Parental_Involvement` | Level of parental involvement |
| `Access_to_Resources` | Availability of learning resources |
| `Extracurricular_Activities` | Participation in extracurricular activities |
| `Sleep_Hours` | Average number of sleeping hours |
| `Previous_Scores` | Previous academic scores |
| `Motivation_Level` | Student motivation level |
| `Internet_Access` | Availability of internet access |
| `Tutoring_Sessions` | Number of tutoring sessions |
| `Family_Income` | Family income category |
| `Teacher_Quality` | Teacher quality |
| `School_Type` | Type of school |
| `Peer_Influence` | Influence of peers |
| `Physical_Activity` | Physical activity level |
| `Learning_Disabilities` | Learning disability information |
| `Parental_Education_Level` | Parent education level |
| `Distance_from_Home` | Distance from home |
| `Gender` | Student gender |
| `Exam_Score` | Student examination score |

---

# 🧹 Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the dataset using Pandas.
2. Checked the dataset shape and structure.
3. Examined data types.
4. Checked for missing values.
5. Checked for duplicate records.
6. Handled missing categorical values using the mode.
7. Separated features and target variable.
8. Identified numerical and categorical features.
9. Applied One-Hot Encoding to categorical variables.
10. Created a preprocessing pipeline.
11. Split the dataset into training and testing data.

### Train-Test Split

The dataset was divided using an **80:20 ratio**.

```text
Training Samples : 5285
Testing Samples  : 1322
