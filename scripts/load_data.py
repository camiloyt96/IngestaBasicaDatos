#script load_data.py

import pandas as pd
import os 

#Rutas 

RAW_PATH = os.path.join("data","raw data", "riesgo_hipertension_dataset.csv")

def load_data(path: str) -> pd.DataFrame:
    #Carga el csv de forma basica 

    print("Ingesta de datos Hipertension")

    #Cargar 
    df = pd.read_csv(path)
    print(f"Archivo cargado {path}")

    #Dimensiones 
    print(f"\n Shape: {df.shape[0]} filas x {df.shape[1]} columnas")

    #valores nulos 
    nulls = df.isnull().sum()
    print(f"Valores nulos por columna")

    if nulls.sum() == 0:
        print(f"No hay valores nulos")
    else:
        print(nulls[nulls>0].to_string())

    print("Carga completa")

    return df

if __name__ == "__main__":
    df = load_data(RAW_PATH)

