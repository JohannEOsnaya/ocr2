from fastapi import APIRouter
from models.red import Red
from helpers.inter import interpretacion_cita
from helpers.model import new_model as model

red = APIRouter()

@red.post('/red', response_model= str, tags=["Text"])
def testDeRed(red: Red):
    analisis = model.predict(red.citas)
    return interpretacion_cita(analisis)