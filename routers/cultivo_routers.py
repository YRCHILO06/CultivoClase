
from fastapi import APIRouter

from schemas.cultivo_schemas import PatientData
from services.cultivo_services import diabetes_prediction


router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Hello Word"}

@router.post("/predict")
async def patient_predict(data: PatientData):
    print("patient data ", data.identification_number)



    prediction = diabetes_prediction(data)

    return {"prediction": prediction}