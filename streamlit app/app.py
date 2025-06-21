import streamlit as st
import helper
import joblib

# model = joblib.load('tfidf_randomforest.joblib')
model = joblib.load('cv_randomforest.joblib')
st.header("Duplicate Question Pairs")

q1 = st.text_input("Enter question 1")
q2 = st.text_input("Enter question 2")

if st.button('Find'):
    query = helper.query_point_creator(q1, q2)
    result = model.predict(query)[0]
    if result==0:
        # st.code("Questions are not duplicate.", language='text')
        st.markdown(
                                '''<h4 style='text-align: left; color: #1ed760;'>Questions are not duplicate.</h4>''',
                                unsafe_allow_html=True)
    else:
        # st.code("Question are duplicate.", language='text')
        st.markdown('''<h4 style='text-align: left; color: #FF0000;'>Questions are duplicate.</h4>''',
                                unsafe_allow_html=True)