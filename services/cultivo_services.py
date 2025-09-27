
import pickle
import numpy as np
from schemas.cultivo_schemas import PatientData

with open('RFCultivoV01.pkl','rb') as file:
    RF_model2 = pickle.load(file)


labels = ["Sano", "Enfermo"]

def diabetes_prediction(data: PatientData):

    xin = np.array([
        data.pregnancies,
        data.glucose,
        data.bloodPressure,
        data.skinThickness,
        data.insulin,
        data.bmi,
        data.diabetesPedigreeFunction,
        data.age,
    ]).reshape(1,8)

    prediction = RF_model2.predict(xin)

    print("prediccion", prediction)

    return labels[prediction[0]]