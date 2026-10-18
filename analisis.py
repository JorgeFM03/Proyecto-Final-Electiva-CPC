from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

RUTA_DATOS = Path(__file__).resolve().parent / "export.csv"
FILAS_MUESTRA = 1000


def cargar_datos(ruta: Path = RUTA_DATOS, nrows: int | None = None) -> pd.DataFrame:
    extension = ruta.suffix.lower()
    if extension == ".csv":
        return pd.read_csv(ruta, nrows=nrows)
    if extension in {".xlsx", ".xls"}:
        return pd.read_excel(ruta, nrows=nrows)
    raise ValueError(f"Formato no admitido: {extension}. Usa CSV o Excel.")


def main() -> None:
    datos = cargar_datos(nrows=FILAS_MUESTRA)
    print(f"Archivo: {RUTA_DATOS.name}")
    print(f"Filas analizadas: {len(datos)}")
    print(f"Columnas: {datos.columns.tolist()}")
    print("Valores nulos por columna:")
    print(datos.isna().sum().sort_values(ascending=False).to_string())


if __name__ == "__main__":
    main()