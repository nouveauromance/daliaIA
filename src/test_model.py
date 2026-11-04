import joblib
import pandas as pd

modelo = joblib.load("src/modelo_final.joblib")

dados = pd.DataFrame([{
    "Age": 27,
    "SystolicBP": 120,
    "DiastolicBP": 80,
    "BS": 8,
    "BodyTemp": 98,
    "HeartRate": 75
}])

previsao = modelo.predict(dados)

print("Previsão:", previsao[0])