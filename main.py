from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

#Modelo de mensaje

class Mensaje(BaseModel):
    user : str
    mensaje: str

class MensajeConID(Mensaje):
    id : int

#Base de datos simulada

mensajes: List[MensajeConID] = []
contador_id = 1

