
import pickle
import numpy as np
from schemas.cultivo_schemas import PatientData

with open('SVMCultivoV01.pkl','rb') as file:
    RF_model2 = pickle.load(file)



labels = ['rice',
 'maize',
 'chickpea',
 'kidneybeans',
 'pigeonpeas',
 'mothbeans',
 'mungbean',
 'blackgram',
 'lentil',
 'pomegranate',
 'banana',
 'mango',
 'grapes',
 'watermelon',
 'muskmelon',
 'apple',
 'orange',
 'papaya',
 'coconut',
 'cotton',
 'jute',
 'coffee']

def diabetes_prediction(data: PatientData):

    xin = np.array([
        data.N,
        data.P,
        data.K,
        data.temperature,
        data.humidity,
        data.ph,
        data.rainfall,
    ]).reshape(1,7)

    prediction = RF_model2.predict(xin)

    print("prediccion", prediction)

    return prediction[0]