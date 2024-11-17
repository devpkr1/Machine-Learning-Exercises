
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open('logistic_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app
st.title('Titanic Survival Prediction')

# User inputs
pclass = st.selectbox('Pclass', [1, 2, 3])
sex = st.selectbox('Sex', ['male', 'female'])
age = st.slider('Age', 0, 100, 25)
sibsp = st.number_input('SibSp (Siblings/Spouses)', 0, 10, 0)
parch = st.number_input('Parch (Parents/Childs)', 0, 10, 0)
fare = st.number_input('Fare', 0.0, 1000.0, 50.0)
embarked = st.selectbox('Embarked', ['C', 'Q', 'S'])

# Encode categorical variables
sex = 1 if sex == 'male' else 0
embarked = {'C': 0, 'Q': 1, 'S': 2}[embarked]

# Create a DataFrame for the input data
input_data = pd.DataFrame({
    'Pclass': [pclass],
    'Sex': [sex],
    'Age': [age],
    'SibSp': [sibsp],
    'Parch': [parch],
    'Fare': [fare],
    'Embarked': [embarked]
})

# Make prediction
prediction = model.predict(input_data)
prediction_proba = model.predict_proba(input_data)[:, 1]

# Display the prediction
if prediction[0] == 1:
    st.success(f'The passenger is likely to survive with a probability of {prediction_proba[0]:.2f}')
else:
    st.error(f'The passenger is not likely to survive with a probability of {prediction_proba[0]:.2f}')


# Add a disclaimer and acknowledgment
st.markdown("""
    ---
    **Disclaimer:** The predictions made by this app are based on a logistic regression model trained on historical Titanic data. The model is provided for educational purposes and should not be used for actual decision-making or relied upon for any critical assessments. The accuracy of predictions can vary and is not guaranteed.

    **Model Designed by:** [Pradeep Kumar](https://www.linkedin.com/in/pradeep-kumar-1722b6123/)
""")
