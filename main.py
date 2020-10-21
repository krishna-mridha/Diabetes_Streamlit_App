import pickle
import streamlit as st
import time
from PIL import Image
from PIL import Image

pickle_in = open("diabetes_model.pkl", "rb")
classifier = pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dbf, age):
    prediction = classifier.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dbf, age]])
    print(prediction)
    return prediction


def main():
    st.write('Please see the top left corner the ">" for getting option')
    age = st.sidebar.number_input("Age in Years", min_value=18, max_value=100)
    pregnancies = st.sidebar.number_input("Number of Pregnancies", value=0, min_value=int(0), max_value=int(50))

    glucose = st.sidebar.slider('Glucose Level', 0, 200, 50)
    skin_thickness = st.sidebar.slider("Skin Thickness", 0, 99, 30)
    blood_pressure = st.sidebar.slider("Blood Pressure", 0, 122, 60)
    insulin = st.sidebar.slider("Insulin", 0, 846, 500)
    bmi = st.sidebar.slider("BMI", 0.0, 67.10, 20.9)
    dbf = st.sidebar.slider("Diabetes Pedigree Function", 0.00, 2.42, 0.50)

    html_temp = """
        <div style="background-color:tomato;padding:10px">
        <h5 style="color:white;text-align:center;">Prediction fo Diabetes with ML App </h5>
        </div>
        """

    st.markdown(html_temp, unsafe_allow_html=True)
    image = Image.open('diabetes.png')
    st.image(image, use_column_width=True)

    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dbf,
                                             age)

        with st.spinner('Wait for it...'):
            time.sleep(1)
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.1)
            progress.progress(i + 1)
        st.success('Done!')
        if result:
            st.warning('Ohh! You have diabetes')
        else:
            st.success('Ohh! Great, You are safe from diabetes')
            st.balloons()



if __name__ == '__main__':
    main()
