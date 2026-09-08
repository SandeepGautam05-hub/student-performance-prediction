import streamlit as st  # type: ignore[import-not-found]
import pandas as pd

try:
    import joblib  # type: ignore[import-not-found]
except ModuleNotFoundError:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "joblib"])
    import joblib  # type: ignore[import-not-found]


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)


# ==========================================
# LOAD TRAINED MODEL
# ==========================================

model = joblib.load("model/student_model.pkl")


# ==========================================
# TITLE
# ==========================================

st.title("🎓 Student Performance Prediction")

st.write(
    "Enter the student's information to predict their expected exam score."
)

st.caption(
    "This machine learning application predicts student exam performance "
    "using academic, behavioral, and demographic factors."
)

st.divider()


# ==========================================
# ACADEMIC INFORMATION
# ==========================================

st.subheader("📚 Academic Information")

col1, col2 = st.columns(2)


with col1:

    hours_studied = st.slider(
        "Hours Studied",
        min_value=1,
        max_value=24,
        value=20
    )

    attendance = st.slider(
        "Attendance (%)",
        min_value=0,
        max_value=100,
        value=80
    )

    previous_scores = st.slider(
        "Previous Scores",
        min_value=0,
        max_value=100,
        value=70
    )


with col2:

    sleep_hours = st.slider(
        "Sleep Hours",
        min_value=0,
        max_value=12,
        value=7
    )

    tutoring_sessions = st.slider(
        "Tutoring Sessions",
        min_value=0,
        max_value=8,
        value=2
    )

    physical_activity = st.slider(
        "Physical Activity (hours/week)",
        min_value=0,
        max_value=10,
        value=3
    )


# ==========================================
# STUDENT INFORMATION
# ==========================================

st.subheader("👨‍🎓 Student Information")

col1, col2 = st.columns(2)


with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    parental_involvement = st.selectbox(
        "Parental Involvement",
        ["Low", "Medium", "High"]
    )

    motivation_level = st.selectbox(
        "Motivation Level",
        ["Low", "Medium", "High"]
    )

    internet_access = st.selectbox(
        "Internet Access",
        ["No", "Yes"]
    )

    extracurricular_activities = st.selectbox(
        "Extracurricular Activities",
        ["No", "Yes"]
    )

    learning_disabilities = st.selectbox(
        "Learning Disabilities",
        ["No", "Yes"]
    )


with col2:

    access_to_resources = st.selectbox(
        "Access to Resources",
        ["Low", "Medium", "High"]
    )

    family_income = st.selectbox(
        "Family Income",
        ["Low", "Medium", "High"]
    )

    teacher_quality = st.selectbox(
        "Teacher Quality",
        ["Low", "Medium", "High"]
    )

    school_type = st.selectbox(
        "School Type",
        ["Public", "Private"]
    )

    peer_influence = st.selectbox(
        "Peer Influence",
        ["Negative", "Neutral", "Positive"]
    )

    parental_education_level = st.selectbox(
        "Parental Education Level",
        ["High School", "College", "Postgraduate"]
    )

    distance_from_home = st.selectbox(
        "Distance From Home",
        ["Near", "Moderate", "Far"]
    )


# ==========================================
# PREDICTION
# ==========================================

st.divider()

if st.button("🎯 Predict Exam Score"):

    # Create DataFrame with all 19 features

    input_data = pd.DataFrame([{

        "Hours_Studied": hours_studied,

        "Attendance": attendance,

        "Parental_Involvement": parental_involvement,

        "Access_to_Resources": access_to_resources,

        "Extracurricular_Activities": extracurricular_activities,

        "Sleep_Hours": sleep_hours,

        "Previous_Scores": previous_scores,

        "Motivation_Level": motivation_level,

        "Internet_Access": internet_access,

        "Tutoring_Sessions": tutoring_sessions,

        "Family_Income": family_income,

        "Teacher_Quality": teacher_quality,

        "School_Type": school_type,

        "Peer_Influence": peer_influence,

        "Physical_Activity": physical_activity,

        "Learning_Disabilities": learning_disabilities,

        "Parental_Education_Level": parental_education_level,

        "Distance_from_Home": distance_from_home,

        "Gender": gender

    }])


    # ======================================
    # MAKE PREDICTION
    # ======================================

    prediction = model.predict(input_data)[0]


    # ======================================
    # DISPLAY PREDICTION
    # ======================================

    st.success(
        f"🎯 Predicted Exam Score: {prediction:.2f}"
    )


    st.write("### 📈 Score Visualization")

    score_for_bar = max(0, min(float(prediction), 100))

    st.progress(score_for_bar / 100)

    st.write(f"Score: {prediction:.2f} / 100")


    # ======================================
    # PERFORMANCE CATEGORY
    # ======================================

    if prediction >= 90:

        performance = "Excellent 🌟"

    elif prediction >= 75:

        performance = "Good 👍"

    elif prediction >= 60:

        performance = "Average 📚"

    else:

        performance = "Needs Improvement 📖"


    st.info(
        f"📊 Performance Level: {performance}"
    )


    # ======================================
    # RECOMMENDATIONS
    # ======================================

    st.subheader("💡 Recommendations")


    recommendation_given = False


    if attendance < 75:

        st.warning(
            "📚 Improve your attendance. Try to maintain attendance above 75%."
        )

        recommendation_given = True


    if hours_studied < 4:

        st.warning(
            "⏰ Try to increase your daily study hours."
        )

        recommendation_given = True


    if previous_scores < 60:

        st.warning(
            "📖 Focus on improving your academic performance."
        )

        recommendation_given = True


    if sleep_hours < 6:

        st.warning(
            "😴 Try to maintain at least 6 hours of sleep."
        )

        recommendation_given = True


    if tutoring_sessions == 0:

        st.warning(
            "👨‍🏫 Consider tutoring sessions if you need additional academic support."
        )

        recommendation_given = True


    if motivation_level == "Low":

        st.warning(
            "💪 Try to improve your motivation and maintain a consistent study routine."
        )

        recommendation_given = True


    if not recommendation_given:

        st.success(
            "🎉 Your study habits look good. Keep up the great work!"
        )


        # ==========================================
# MODEL PERFORMANCE
# ==========================================

st.divider()

st.subheader("📊 Model Performance")

st.write(
    "Two regression models were trained and evaluated "
    "using the same test dataset."
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("### Linear Regression")

    st.metric(
        "MAE",
        "0.45"
    )

    st.metric(
        "RMSE",
        "1.80"
    )

    st.metric(
        "R² Score",
        "76.96%"
    )


with col2:

    st.markdown("### Random Forest")

    st.metric(
        "MAE",
        "1.09"
    )

    st.metric(
        "RMSE",
        "2.16"
    )

    st.metric(
        "R² Score",
        "66.93%"
    )


st.success(
    "🏆 Selected Model: Linear Regression"
)