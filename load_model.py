import streamlit as st
import pickle
pickle_in = open('pipe_pkl1', 'rb')
pickle_model = pickle.load(pickle_in)
import pandas as pd
new_input = pd.DataFrame({
                     "age":[26],
                     "hypertension":[0], 
                     "heart_disease":[0],
                    "bmi":[20],
                    "HbA1c_level":[4],
                     "blood_glucose_level":[60],
                     "gender_num":[0],
                     "smoking_history_num":[0]
      
})
prediction = pickle_model.predict(new_input)
if (prediction[0]==1):
    st.write("The Person is Diabetic")
else:
    st.write("The Person is Not Diabetic")