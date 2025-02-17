import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px
from datetime import datetime
import random
from datetime import datetime, timedelta

# 1. Configuración inicial de la aplicación

st. set_page_config(
  page_title="Agroindustria en Colombia",
  page_icon="🌳",
  layout="wide"
)

st.title(" 🌳 Agroindustria en Colombia 🌳")
st.sidebar.title(" ☷ Menu Opciones")

import random
from datetime import datetime, timedelta

# Generar datos aleatorios
num_datos = 10

identificacion_proceso = random.sample(range(62, 73), num_datos)
identificacion_producto = random.sample(range(1001, 1012), num_datos)

# Generar fechas aleatorias
def fecha_aleatoria():
    inicio = datetime(2023, 1, 1)
    fin = datetime(2024, 1, 1)
    return inicio + timedelta(days=random.randint(0, (fin - inicio).days))

fechas_inicio = [fecha_aleatoria() for _ in range(num_datos)]
fechas_finalizacion = [fecha + timedelta(days=random.randint(1, 30)) for fecha in fechas_inicio]

tiempo_procesamiento = [random.randint(200, 1000) for _ in range(num_datos)]
costo_produccion = [random.randint(10000000, 20000000) for _ in range(num_datos)]

# Crear DataFrame
df = pd.DataFrame({
    "Identificación Proceso": identificacion_proceso,
    "Identificación Producto": identificacion_producto,
    "Fecha de Inicio": fechas_inicio,
    "Fecha de Finalización": fechas_finalizacion,
    "Tiempo de Procesamiento (min)": tiempo_procesamiento,
    "Costo de Producción ($)": costo_produccion
})


