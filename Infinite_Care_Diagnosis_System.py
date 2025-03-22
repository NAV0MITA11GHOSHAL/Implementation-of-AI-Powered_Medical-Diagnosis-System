import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Name & Logo
st.set_page_config(page_title="Infinite Care Diagnosis System", page_icon="🩺")

# ----HEADER SECTION ----
with st.container():
    st.title(":blue[Infinite Care Diagnosis System]")
    st.markdown('<p style="color: white; font-size: 20px;">Welcome to Infinite Care Diagnosis System, a one-stop solution to diagnose disease.</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: white; font-size: 18px;">Rest Assured! This website is designed to be completely anonymous. No user data is stored on our servers.</p>', unsafe_allow_html=True)

# Hiding Streamlit add-ons
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Adding Background Image
background_image_url = "./Doctors_Using_AI.jpg"

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url({background_image_url});
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stAppViewContainer"]::before {{
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(0, 0, 0, 0.70);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load the saved models
models = {
    'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
}


# Create diagnosis report
def custom_success(message):
        st.markdown(f"""<div style="background-color: #D4EDDA; color: #155724; padding: 10px; border-radius: 5px;">{message}</div>""", unsafe_allow_html=True)


# Create a dropdown menu for disease prediction
with st.container():
    selected = st.selectbox(
        ':red[**Select a Disease to Predict**]',
        ['Diabetes Prediction','Heart Disease Prediction', 'Parkinsons Prediction', 'Lung Cancer Prediction', 'Hypo-Thyroid Prediction']
    )

def display_input(label, tooltip, key, type="text"):
    if type == "text":
        return st.text_input(label, key=key, help=tooltip)
    elif type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    with st.container():
        st.markdown('<h2 style="color: white;">Diabetes</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color: white;">Enter the following details to predict diabetes:</p>', unsafe_allow_html=True)
        left_column, right_column = st.columns(2)
        with left_column:
            Pregnancies = display_input(':red[**Number of Pregnancies**]', 'Enter number of times pregnant', 'Pregnancies', 'number')
            Glucose = display_input(':red[**Glucose Level**]', 'Enter glucose level', 'Glucose', 'number')
            BloodPressure = display_input(':red[**Blood Pressure value**]', 'Enter blood pressure value', 'BloodPressure', 'number')
            SkinThickness = display_input(':red[**Skin Thickness value**]', 'Enter skin thickness value', 'SkinThickness', 'number')
        with right_column:
            Insulin = display_input(':red[**Insulin Level**]', 'Enter insulin level', 'Insulin', 'number')
            BMI = display_input(':red[**BMI value**]', 'Enter Body Mass Index value', 'BMI', 'number')
            DiabetesPedigreeFunction = display_input(':red[**Diabetes Pedigree Function value**]', 'Enter diabetes pedigree function value', 'DiabetesPedigreeFunction', 'number')
            Age = display_input(':red[**Age of the Person**]', 'Enter age of the person', 'Age', 'number')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        diab_prediction = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        custom_success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    with st.container():
        st.markdown('<h2 style="color: white;">Heart Disease</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color: white;">Enter the following details to predict heart disease:</p>', unsafe_allow_html=True)
        left_column, right_column = st.columns(2)
        with left_column:
            age = display_input(':red[**Age**]', 'Enter age of the person', 'age', 'number')
            trestbps = display_input(':red[**Resting Blood Pressure**]', 'Enter resting blood pressure', 'trestbps', 'number')
            chol = display_input(':red[**Serum Cholesterol in mg/dl**]', 'Enter serum cholesterol', 'chol', 'number')
            fbs = display_input(':red[**Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)**]', 'Enter fasting blood sugar', 'fbs', 'number')
            cp = display_input(':red[**Chest Pain types (0, 1, 2, 3)**]', 'Enter chest pain type', 'cp', 'number')
            exang = display_input(':red[**Exercise Induced Angina (1 = yes; 0 = no)**]', 'Enter exercise induced angina', 'exang', 'number')
            restecg = display_input(':red[**Resting Electrocardiographic results (0, 1, 2)**]', 'Enter resting ECG results', 'restecg', 'number')
            
            with right_column:
                sex = display_input(':red[**Sex (1 = male; 0 = female)**]', 'Enter sex of the person', 'sex', 'number')
                thalach = display_input(':red[**Maximum Heart Rate achieved**]', 'Enter maximum heart rate', 'thalach', 'number')
                ca = display_input(':red[**Major vessels colored by fluoroscopy (0-3)**]', 'Enter number of major vessels', 'ca', 'number')
                thal = display_input(':red[**Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)**]', 'Enter thal value', 'thal', 'number')
                slope = display_input(':red[**Slope of the peak exercise ST segment (0, 1, 2)**]', 'Enter slope value', 'slope', 'number')
                oldpeak = display_input(':red[**ST depression induced by exercise**]', 'Enter ST depression value', 'oldpeak', 'number')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        heart_prediction = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
        custom_success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    with st.container():
        st.markdown('<h2 style="color: white;">Parkinson&#39;s Disease</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color: white;">Enter the following details to predict Parkinson&#39;s disease:</p>', unsafe_allow_html=True)
        left_column, right_column = st.columns(2)
        with left_column:
            fo = display_input(':red[**MDVP:Fo(Hz)**]', 'Enter MDVP:Fo(Hz) value', 'fo', 'number')
            flo = display_input(':red[**MDVP:Flo(Hz)**]', 'Enter MDVP:Flo(Hz) value', 'flo', 'number')
            Jitter_percent = display_input(':red[**MDVP:Jitter(%)**]', 'Enter MDVP:Jitter(%) value', 'Jitter_percent', 'number')
            DFA = display_input(':red[**DFA', 'Enter DFA value**]', 'DFA', 'number')
            RAP = display_input(':red[**MDVP:RAP**]', 'Enter MDVP:RAP value', 'RAP', 'number')
            PPQ = display_input(':red[**MDVP:PPQ**]', 'Enter MDVP:PPQ value', 'PPQ', 'number')
            APQ3 = display_input(':red[**Shimmer:APQ3**]', 'Enter Shimmer:APQ3 value', 'APQ3', 'number')
            DDP = display_input(':red[**Jitter:DDP**]', 'Enter Jitter:DDP value', 'DDP', 'number')
            Shimmer = display_input(':red[**MDVP:Shimmer**]', 'Enter MDVP:Shimmer value', 'Shimmer', 'number')
            NHR = display_input(':red[**NHR**]', 'Enter NHR value', 'NHR', 'number')
            spread1 = display_input(':red[**Spread1**]', 'Enter spread1 value', 'spread1', 'number')

            with right_column:
                fhi = display_input(':red[**MDVP:Fhi(Hz)**]', 'Enter MDVP:Fhi(Hz) value', 'fhi', 'number')
                D2 = display_input(':red[**D2**]', 'Enter D2 value', 'D2', 'number')
                Jitter_Abs = display_input(':red[**MDVP:Jitter(Abs)**]', 'Enter MDVP:Jitter(Abs) value', 'Jitter_Abs', 'number')
                RPDE = display_input(':red[**RPDE**]', 'Enter RPDE value', 'RPDE', 'number')
                PPE = display_input(':red[**PPE**]', 'Enter PPE value', 'PPE', 'number')
                APQ = display_input(':red[**MDVP:APQ**]', 'Enter MDVP:APQ value', 'APQ', 'number')
                APQ5 = display_input(':red[**Shimmer:APQ5**]', 'Enter Shimmer:APQ5 value', 'APQ5', 'number')
                DDA = display_input(':red[**Shimmer:DDA**]', 'Enter Shimmer:DDA value', 'DDA', 'number')
                Shimmer_dB = display_input(':red[**MDVP:Shimmer(dB)**]', 'Enter MDVP:Shimmer(dB) value', 'Shimmer_dB', 'number')
                HNR = display_input(':red[**HNR**]', 'Enter HNR value', 'HNR', 'number')
                spread2 = display_input(':red[**Spread2**]', 'Enter spread2 value', 'spread2', 'number')

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Disease Test Result"):
        parkinsons_prediction = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        custom_success(parkinsons_diagnosis)

# Lung Cancer Prediction Page
if selected == "Lung Cancer Prediction":
    with st.container():
        st.markdown('<h2 style="color: white;">Lung Cancer</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color: white;">Enter the following details to predict lung cancer:</p>', unsafe_allow_html=True)
        left_column, right_column = st.columns(2)
        with left_column:
            GENDER = display_input(':red[**Gender (1 = Male; 0 = Female)**]', 'Enter gender of the person', 'GENDER', 'number')
            ANXIETY = display_input(':red[**Anxiety (2 = Yes; 1 = No)**]', 'Enter if the person has anxiety', 'ANXIETY', 'number')
            ALCOHOL_CONSUMING = display_input(':red[**Alcohol Consuming (2 = Yes; 1 = No)**]', 'Enter if the person consumes alcohol', 'ALCOHOL_CONSUMING', 'number')
            ALLERGY = display_input(':red[**Allergy (2 = Yes; 1 = No)**]', 'Enter if the person has allergies', 'ALLERGY', 'number')
            COUGHING = display_input(':red[**Coughing (2 = Yes; 1 = No)**]', 'Enter if the person experiences coughing', 'COUGHING', 'number')
            SWALLOWING_DIFFICULTY = display_input(':red[**Swallowing Difficulty (2 = Yes; 1 = No)**]', 'Enter if the person has difficulty swallowing', 'SWALLOWING_DIFFICULTY', 'number')
            FATIGUE = display_input(':red[**Fatigue (2 = Yes; 1 = No)**]', 'Enter if the person experiences fatigue', 'FATIGUE', 'number')
            CHRONIC_DISEASE = display_input(':red[**Chronic Disease (2 = Yes; 1 = No)**]', 'Enter if the person has a chronic disease', 'CHRONIC_DISEASE', 'number')

        with right_column:
            AGE = display_input(':red[**Age**]', 'Enter age of the person', 'AGE', 'number')
            PEER_PRESSURE = display_input(':red[**Peer Pressure (2 = Yes; 1 = No)**]', 'Enter if the person is under peer pressure', 'PEER_PRESSURE', 'number')
            SMOKING = display_input(':red[**Smoking (2 = Yes; 1 = No)**]', 'Enter if the person smokes', 'SMOKING', 'number')
            WHEEZING = display_input(':red[**Wheezing (2 = Yes; 1 = No)**]', 'Enter if the person experiences wheezing', 'WHEEZING', 'number')
            SHORTNESS_OF_BREATH = display_input(':red[**Shortness Of Breath (2 = Yes; 1 = No)**]', 'Enter if the person experiences shortness of breath', 'SHORTNESS_OF_BREATH', 'number')
            CHEST_PAIN = display_input(':red[**Chest Pain (2 = Yes; 1 = No)**]', 'Enter if the person experiences chest pain', 'CHEST_PAIN', 'number')
            YELLOW_FINGERS = display_input(':red[**Yellow Fingers (2 = Yes; 1 = No)**]', 'Enter if the person has yellow fingers', 'YELLOW_FINGERS', 'number')

    lungs_diagnosis = ''
    if st.button("Lung Cancer Test Result"):
        lungs_prediction = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        lungs_diagnosis = "The person has lung cancer disease" if lungs_prediction[0] == 1 else "The person does not have lung cancer disease"
        custom_success(lungs_diagnosis)

# Hypo-Thyroid Prediction Page
if selected == "Hypo-Thyroid Prediction":
    with st.container():
        st.markdown('<h2 style="color: white;">Hypo-Thyroid</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color: white;">Enter the following details to predict hypo-thyroid disease:</p>', unsafe_allow_html=True)
        left_column, right_column = st.columns(2)
        with left_column:
            age = display_input(':red[**Age**]', 'Enter age of the person', 'age', 'number')
            on_thyroxine = display_input(':red[**On Thyroxine (1 = Yes; 0 = No)**]', 'Enter if the person is on thyroxine', 'on_thyroxine', 'number')
            t3_measured = display_input(':red[**T3 Measured (1 = Yes; 0 = No)**]', 'Enter if T3 was measured', 't3_measured', 'number')
            tt4 = display_input(':red[**TT4 Level**]', 'Enter TT4 level', 'tt4', 'number')

        with right_column:
            sex = display_input(':red[**Sex (1 = Male; 0 = Female)**]', 'Enter sex of the person', 'sex', 'number')
            tsh = display_input(':red[**TSH Level**]', 'Enter TSH level', 'tsh', 'number')
            t3 = display_input(':red[**T3 Level**]', 'Enter T3 level', 't3', 'number')

    thyroid_diagnosis = ''
    if st.button("Thyroid Test Result"):
        thyroid_prediction = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
        thyroid_diagnosis = "The person has Hypo-Thyroid disease" if thyroid_prediction[0] == 1 else "The person does not have Hypo-Thyroid disease"
        custom_success(thyroid_diagnosis)



# ----FOOTER SECTION ----
with st.container():
    st.markdown("""
    <style>
    .footer {
        left: 0;
        bottom: 0;
        width: 100%;
        display: flex;
        justify-content: space-between; /* Space between left and right */
        color: #fff;
        font-size: 24px; /* Footer text size */
    }
    .footer a {
        margin-left: 15px;
        text-decoration: none;
        color: #fff;
        font-size: 24px; /* Icon size */
    }
    </style>
    <div class="footer">
        <div class="footer-left">
            <p>Infinite Care Diagnosis System <sup>&copy;</sup> 2025</p>
        </div>
        <div class="footer-right">
            <a href="https://github.com/NAV0MITA11GHOSHAL" target="_blank">
                <i class="fa-brands fa-github"></i>
            </a>
        </div>
    </div>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css" />
    """, unsafe_allow_html=True)
