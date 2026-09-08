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

### The project includes:

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
The main objectives of this project are:

1. Analyze factors affecting student examination performance.
2. Perform data cleaning and preprocessing.
3. Explore relationships between different student factors and exam scores.
4. Train multiple machine learning regression models.
5. Compare model performance using evaluation metrics.
6. Select the best-performing model.
7. Build an interactive Streamlit application.
8. Deploy the application online for public access.

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
<<<<<<< HEAD
=======

```
### 🤖 Machine Learning Models

Two regression algorithms were trained and evaluated.

1. Linear Regression

Linear Regression was used for predicting student exam scores.

Performance :
MAE  : 0.45
RMSE : 1.80
R²   : 0.7696

2. Random Forest Regressor

Random Forest Regression was trained to compare its performance with Linear Regression.

Performance :
MAE  : 1.09
RMSE : 2.16
R²   : 0.6693 

```markdown
### 🏆 Model Comparison

| Model | MAE ↓ | RMSE ↓ | R² ↑ |
|---|---:|---:|---:|
| Linear Regression | 0.45 | 1.80 | 0.7696 |
| Random Forest Regressor | 1.09 | 2.16 | 0.6693 |

### 🏆 Final Model

Linear Regression was selected as the final model because it achieved:

- Lower Mean Absolute Error (MAE)
- Lower Root Mean Squared Error (RMSE)
- Higher R² Score

The final trained model was saved using Joblib:
model/student_model.pkl


### 📈 Exploratory Data Analysis

Exploratory Data Analysis was performed using:

Pandas
Matplotlib
Seaborn

The following visualizations were created:

1. Exam Score Distribution

A histogram was used to understand the distribution of student examination scores.

2. Hours Studied vs Exam Score

A scatter plot was used to analyze the relationship between study hours and exam scores.

Observation: Students who studied more hours generally showed higher exam scores.

3. Attendance vs Exam Score

A scatter plot was used to analyze the relationship between attendance and exam performance.

Observation: Attendance showed a strong positive relationship with exam scores.

4. Previous Scores vs Exam Score

A scatter plot was used to compare previous academic performance with current examination scores.

5. Motivation Level vs Exam Score

A box plot was used to compare exam scores across different motivation levels.

6. Parental Involvement vs Exam Score

A box plot was used to compare exam scores based on parental involvement.

7. Correlation Heatmap

A correlation heatmap was created to analyze relationships between numerical variables.


### 📊 Important EDA Findings

The numerical features with the strongest relationships with Exam_Score were:

| Feature           | Correlation with Exam Score |
| ----------------- | --------------------------: |
| **Attendance**    |                   **0.581** |
| **Hours Studied** |                   **0.445** |
| Previous Scores   |                       0.175 |
| Tutoring Sessions |                       0.157 |
| Physical Activity |                       0.028 |
| Sleep Hours       |                      -0.017 |


## Key Observations

📚 Attendance had the strongest positive correlation with exam scores.
⏰ Hours Studied also showed a strong positive relationship with exam scores.
📝 Previous Scores showed a smaller positive relationship.
👨‍👩‍👧 Parental Involvement showed slightly higher average scores at higher involvement levels.
📊 Correlation represents association and does not necessarily imply causation.

### 🏗️ Project Architecture

                         ┌─────────────────────┐
                         │    Kaggle Dataset   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  Data Exploration   │
                         │     & Cleaning      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Feature Preparation │
                         │    & Encoding       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Train/Test Split  │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    ▼                               ▼
          ┌──────────────────┐             ┌──────────────────┐
          │ Linear Regression│             │  Random Forest   │
          └────────┬─────────┘             └────────┬─────────┘
                   │                                │
                   └───────────────┬────────────────┘
                                   ▼
                         ┌─────────────────────┐
                         │  Model Evaluation   │
                         │   MAE / RMSE / R²   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  Model Comparison   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Linear Regression   │
                         │      Selected       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ student_model.pkl   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Streamlit App     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Student Inputs    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Predicted Exam Score│
                         └──────────┬──────────┘
                                    │
                         ┌──────────┴──────────┐
                         ▼                     ▼
                ┌──────────────────┐  ┌──────────────────┐
                │Performance Level │  │ Recommendations  │
                └──────────────────┘  └──────────────────┘

### 🔄 Complete Project Workflow

Kaggle Dataset
      ↓
Data Loading
      ↓
Data Exploration
      ↓
Data Cleaning
      ↓
Missing Value Handling
      ↓
Feature & Target Separation
      ↓
Categorical Feature Encoding
      ↓
Train-Test Split
      ↓
Train Machine Learning Models
      ↓
Linear Regression + Random Forest
      ↓
Model Evaluation
      ↓
Model Comparison
      ↓
Linear Regression Selected
      ↓
Save Trained Model
      ↓
Build Streamlit Application
      ↓
Take Student Input
      ↓
Predict Exam Score
      ↓
Performance Classification
      ↓
Personalized Recommendations
      ↓
Deploy Application
      ↓
Live Streamlit Application

### 📁 Project Structure

Student Performance Prediction/
│
├── 📂 dataset/
│   └── Dataset.csv
│
├── 📂 model/
│   └── student_model.pkl
│
├── 📂 notebooks/
│   └── student_analysis.ipynb
│
├── 📄 app.py
├── 📄 train_model.py
├── 📄 requirements.txt
├── 📄 README.md
└── 📄 .gitignore

## File & Folder Description

| File / Folder      | Purpose                                     |
| ------------------ | ------------------------------------------- |
| `dataset/`         | Contains the student performance dataset    |
| `model/`           | Contains the trained machine learning model |
| `notebooks/`       | Contains EDA and data analysis              |
| `app.py`           | Streamlit web application                   |
| `train_model.py`   | Model training and evaluation               |
| `requirements.txt` | Required Python libraries                   |
| `README.md`        | Project documentation                       |
| `.gitignore`       | Files excluded from Git                     |


### 🌐 Streamlit Application

The trained machine learning model is integrated into an interactive Streamlit web application.

# 📚 Academic Information

Users can enter:

Hours Studied
Attendance
Previous Scores
Tutoring Sessions

# 🧠 Behavioral Information

Users can enter:

Sleep Hours
Motivation Level
Physical Activity
Extracurricular Activities

# 👨‍🎓 Student Information

Users can enter:

Gender
Parental Involvement
Parental Education Level
Family Income
Access to Resources
Teacher Quality
Peer Influence
Internet Access
Learning Disabilities
School Type
Distance From Home

# Application Output

The application provides:

🎯 Predicted Exam Score
📊 Performance Category
📈 Score Visualization
💡 Personalized Recommendations

### 🎯 Performance Categories

| Predicted Score | Performance Level    |
| --------------: | -------------------- |
|        90 – 100 | 🏆 Excellent         |
|         75 – 89 | 🟢 Good              |
|         60 – 74 | 🟡 Average           |
|        Below 60 | 🔴 Needs Improvement |


### 💡 Personalized Recommendations

The application generates recommendations based on student inputs.

Examples include:

📅 Improve attendance if attendance is low.
📚 Increase study hours if study time is low.
📝 Focus on academic fundamentals if previous scores are low.
😴 Maintain healthy sleep habits.
👨‍🏫 Consider additional tutoring support.
🎯 Develop consistent study habits to improve motivation.

### 🛠️ Technologies Used

| Technology                | Purpose                   |
| ------------------------- | ------------------------- |
| Python                    | Programming language      |
| Pandas                    | Data manipulation         |
| NumPy                     | Numerical operations      |
| Scikit-learn              | Machine learning          |
| Matplotlib                | Data visualization        |
| Seaborn                   | Statistical visualization |
| Joblib                    | Model serialization       |
| Streamlit                 | Web application           |
| Jupyter Notebook          | Data analysis             |
| Git                       | Version control           |
| GitHub                    | Code hosting              |
| Streamlit Community Cloud | Deployment                |



### ▶️ How to Run Locally

1. Clone the Repository
</>Bash
git clone https://github.com/SandeepGautam05-hub/student-performance-prediction.git

2. Navigate to the Project Directory
</>Bash
cd student-performance-prediction

3. Create a Virtual Environment
</>Bash
python -m venv venv

4. Activate the Virtual Environment
Windows 
</>Bash
venv\Scripts\activate

5. Install Dependencies
</>Bash
pip install -r requirements.txt

6. Run the Streamlit Application
</>Bash
streamlit run app.py
The application will open in your web browser.

### 🧪 Model Training

To retrain the machine learning models, run:

python train_model.py
The trained model will be saved as:
model/student_model.pkl

### 📓 Jupyter Notebook

The complete Exploratory Data Analysis is available in:
notebooks/student_analysis.ipynb

The notebook contains:

Dataset exploration
Dataset information
Missing value analysis
Statistical analysis
Exam score distribution
Scatter plots
Box plots
Correlation analysis
Correlation heatmap
Grouped analysis


### 📈 Model Evaluation Metrics

The project uses three important regression evaluation metrics.

# Mean Absolute Error (MAE)

MAE measures the average absolute difference between actual and predicted values.

Lower MAE is better.

# Root Mean Squared Error (RMSE)

RMSE measures the square root of the average squared prediction error.

Lower RMSE is better.

# R² Score

R² measures how much variation in the target variable is explained by the model.

Higher R² is better.

### 📌 Final Project Results
The final selected model was Linear Regression.

MAE  : 0.45
RMSE : 1.80
R²   : 0.7696

The model achieved an R² score of approximately 76.96%, meaning it explains a substantial portion of the variation in exam scores in the test dataset.

### 📸 Project Visualizations

The project includes several visualizations generated during Exploratory Data Analysis:

📊 Exam Score Distribution
📈 Hours Studied vs Exam Score
📈 Attendance vs Exam Score
📈 Previous Scores vs Exam Score
📦 Motivation Level vs Exam Score
📦 Parental Involvement vs Exam Score
🔥 Correlation Heatmap

All EDA visualizations are available in:
notebooks/student_analysis.ipynb


### 🚀 Future Improvements

The project can be improved further by implementing:

Hyperparameter tuning
Cross-validation
Feature importance analysis
Additional regression algorithms
XGBoost / Gradient Boosting
Improved UI/UX
Interactive EDA dashboard
Prediction history
Student performance tracking
Database integration
User authentication
Cloud-based data storage
More advanced recommendation systems

### 📚 Learning Outcomes

Through this project, I implemented and learned:

Data preprocessing
Missing value handling
Categorical feature encoding
Exploratory Data Analysis
Data visualization
Regression algorithms
Train-test splitting
Model evaluation
MAE, RMSE and R²
Scikit-learn pipelines
Model serialization using Joblib
Streamlit application development
Git and GitHub
Cloud deployment


### 👨‍💻 Author
# Sandeep Gautam

# B.Tech – Artificial Intelligence & Machine Learning

🔗 Project Links

## 🚀 Live Application:
https://sandeep-student-performance-predictor-ml.streamlit.app/

## 💻 GitHub Repository:
https://github.com/SandeepGautam05-hub/student-performance-prediction

⭐ If you found this project useful, consider giving the repository a star!


### 📌 Disclaimer

This project is developed for educational and demonstration purposes.

The predictions are based on patterns learned from the provided dataset and should not be considered a definitive assessment of a student's actual academic performance.
