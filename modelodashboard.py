import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px
from datetime import datetime
from datetime import datetime, timedelta

# 1. Configuración inicial de la aplicación

st. set_page_config(
  page_title="Agroindustria en Colombia",
  page_icon="🌳",
  layout="wide"
)

st.title(" 🌳 Agroindustria en Colombia 🌳")
st.sidebar.title(" ☷ Menu Opciones")

# 2. Generación de Datos Aleatorios
np.random.seed(42)
data = pd.DataFrame({
    "Fecha Inicio": pd.date_range(start="2024-01-01", periods=100, freq="D"),
    "Ventas de Insumos": np.random.randint(100, 500, size=100),
    "Categorias de Productos": np.random.choice(["A", "B", "C", "D"], size=100),
    "Hectareas": np.random.uniform(5, 30, size=100),
    "Modelos de Produccion": np.random.randint(1, 10, size=100),
    "Región": np.random.choice(["Norte", "Sur", "Este", "Oeste"], size=100)
})


# 3. Implementación de la Barra de Navegación
menu = st.sidebar.radio(
    "Selecciona una opción:",
    ["Inicio", "Datos", "Visualización", "Configuración"]
)

# 4. Mostrar los Datos
if menu == "Datos":
    st.subheader("📂 Datos Generados")
    st.dataframe(data)




