
from pydantic import BaseModel

class PatientData(BaseModel):
    N: int
    P: int
    K: int
    temperature: float
    humidity: float
    ph: float
    rainfall:float
    
