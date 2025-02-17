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

