from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

modelo = joblib.load("src/modelo_final.joblib")


class DadosGestante(BaseModel):
    Age: float
    SystolicBP: float
    DiastolicBP: float
    BS: float
    BodyTemp: float
    HeartRate: float


@app.get("/")
def inicio():
    return {"mensagem": "Dália está funcionando!"}


@app.post("/predict")
def prever(dados: DadosGestante):

    entrada = pd.DataFrame([{
        "Age": dados.Age,
        "SystolicBP": dados.SystolicBP,
        "DiastolicBP": dados.DiastolicBP,
        "BS": dados.BS,
        "BodyTemp": dados.BodyTemp,
        "HeartRate": dados.HeartRate
    }])

    previsao = modelo.predict(entrada)

    return {
        "previsao": previsao[0]
    }