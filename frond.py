import streamlit as st
import pickle

# Load trained model
with open("asd_model.pkl", "rb") as f:
    model = pickle.load(f)


#st.title("ASD Assessment Form")
import streamlit as st

st.markdown("<h1 style='color: #FF5733; text-align: center;'>ASD Assessment Form</h1>", unsafe_allow_html=True)


# Function to convert Yes/No to 1/0
def yes_no(val):
    return 1 if val == "Yes" else 0

def clean_gender(v):
    if v in ["F", "Female"]:
        return 0
    elif v in ["M", "Male"]:
        return 1

def clean_family(da):
    if da in ["Y", "Yes"]:
        return 0
    elif da in ["N", "No"]:
        return 1


# Input fields
age = st.number_input("Age", min_value=1, step=1)

gender = clean_gender(st.radio("Select Gender", ["Female", "Male"]))
family_history = clean_family(st.selectbox("Family History",["Yes","No"]))

eye_contact = yes_no(st.selectbox("Eye contact", ["Yes", "No"]))
person_alone = yes_no(st.selectbox("Person alone", ["Yes", "No"]))
understand_emotion = yes_no(st.selectbox("Understanding emotion", ["Yes", "No"]))
same_actions = yes_no(st.selectbox("Same actions", ["Yes", "No"]))
social_communication = yes_no(st.selectbox("Social communication", ["Yes", "No"]))
facial_expression = yes_no(st.selectbox("Facial expression", ["Yes", "No"]))
upset_small_change = yes_no(st.selectbox("Upset with small change", ["Yes", "No"]))
sensory_reaction = yes_no(st.selectbox("Sensory reaction", ["Yes", "No"]))
make_friend = yes_no(st.selectbox("Make friend", ["Yes", "No"]))
specific_interests = yes_no(st.selectbox("Specific interests", ["Yes", "No"]))

# Prepare input for model
input_data = [[
    age,
    gender,
    family_history,
    eye_contact,
    person_alone,
    understand_emotion,
    same_actions,
    social_communication,
    facial_expression,
    upset_small_change,
    sensory_reaction,
    make_friend,
    specific_interests
]]

# Submit button
if st.button("Submit"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("High risk of Autism Spectrum Disorder")
    else:
        st.success("Low risk of Autism Spectrum Disorder")

