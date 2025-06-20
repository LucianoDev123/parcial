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

#GET para obtener mensajes

@app.get("/mensajes/{mensaje_id}"), response_model=MensajeConID
def obtener_mensaje(mensaje_id: int):
    for mensaje in mensajes:
        if mensaje.id == mensaje_id:
            return mensaje
    raise HTTPException(status_code=404, detail="No hay mensajes para mostrar")

#POST Para agregr mensajes

@app.post("/mensajes", response_model=MensajeConID, status_code=201)
def crear_mensaje(mensaje:Mensaje):
    global contador_id
    nuevo_mensaje = MensajeConID(id=contador_id, **mensaje.dict())
    mensajes.append(nuevo_mensaje)
    contador_id += 1
    return nuevo_mensaje

# PUT para actualizar mensajes
@app.put("/mensajes/{mensaje_id}", response_model=MensajeConID)
def actualizar_mensaje(mensaje_id: int, mensaje_actualizado: Mensaje):
    for i, mensaje in enumerate(mensajes):
        if mensaje.id == mensaje_id:
            mensajes[i] = MensajeConID(id=mensaje_id, **mensaje_actualizado.dict())
            return mensajes[i]
    raise HTTPException(status_code=404, detail= "Mensaje no encontrado para actualizar")

#DELETE para eliminar un mensaje
@app.delete("/mensajes/{mensaje_id}")
def eliminar_mensaje(mensaje_id: int):
    for mensaje in mensajes:
        if mensaje.id == mensaje_id:
            mensajes.remove(mensaje)
            return {"mensaje": "Mensaje eliminado"}
    raise HTTPException(status_code=404, detail="Mensaje no encontrado para eliminar")

