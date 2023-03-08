# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:42:55 2023

@author: P028600
"""
import time

start_time = time.time()

import os
import streamlit as st
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import pandas as pd

def get_folder_size(path):
        total = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total += os.path.getsize(fp)
        return total / (1024 ** 3) # convertir a gigabytes
     
def main():
    st.title("Almacenamiento SASSTG de Validación Interna")
    paths = {
        "Ronald": r"\\118.180.60.119\sasstg\VI\Ronald",
        "Eduardo": r"\\118.180.60.119\sasstg\VI\Eduardo",
        "David": r"\\118.180.60.119\sasstg\VI\David",
        "Joaquin": r"\\118.180.60.119\sasstg\VI\Joaquin",
        "Claudia": r"\\118.180.60.119\sasstg\VI\Claudia",
        "Stefany": r"\\118.180.60.119\sasstg\VI\Stefany",
        "Deysi": r"\\118.180.60.119\sasstg\VI\Deysi",
        "Sofia": r"\\118.180.60.119\sasstg\VI\Sofia",
        "Hugo": r"\\118.180.60.119\sasstg\VI\Hugo",
        "Cesar": r"\\118.180.60.119\sasstg\VI\Cesar",
        "Edwin": r"\\118.180.60.119\sasstg\VI\Edwin",
        "Geraldine": r"\\118.180.60.119\sasstg\VI\Geraldine",
        "Enzo": r"\\118.180.60.119\sasstg\VI\Enzo",
        "Dashboards": r"\\118.180.60.119\sasstg\VI\Dashboard",
        "Inputs": r"\\118.180.60.119\sasstg\VI\INPUTS",
        "Malos": r"\\118.180.60.119\sasstg\VI\MALOS",
        "Querys": r"\\118.180.60.119\sasstg\VI\QUERYS"}
       # "facturacion": r"\\118.180.60.119\sasstg\VI\FACTURACION",
    
    espacio_completo = []
    for path in paths.values():
        espacio_completo.append(get_folder_size(path))
        
    espacio_total = 3420 # terabytes en el SASTG convertidos a GB
    
    df = pd.DataFrame({
        "nombres": list(paths.keys()),
        "espacio": espacio_completo,
        "espacio_ocupado": sum(espacio_completo),
        "espacio_total": espacio_total,
    })
    df["sobrante"] = df["espacio_total"] - df["espacio_ocupado"]
    df["prc_sobrante"] = df["sobrante"] / df["espacio_total"]
    df['prc_lleno'] = 1-df['prc_sobrante']
        
    sobrante = df['prc_sobrante'].unique()[0]
    lleno = df['prc_lleno'].unique()[0]

    df2 = pd.DataFrame({'names': ['Sobrante', 'Lleno'], 'values': [sobrante, lleno]})
    
    # Configurar la escala de colores
    colors1 = ['#00B9E8', '#F0F8FF']
    colors2 = ['#0070BB', '#89CFF0', '#003262', '#2072AF','318CE7','0000FF','6699CC',
               '#B9D9EB','#99FFFF','#26619C','#ADD8E6','#73C2FB','#0087BD','87D3F8',
               '#9EB9D4','#0076B6']
    # Creando una figura con sos subplots
    fig = make_subplots(rows=1, cols=2,subplot_titles=('Cantidad de Gigabytes (GB) ocupado en el SASSTG', 'Porcentaje de espacio ocupado por colaborador en el SASSTG'), column_width=[0.5, 0.5],specs=[[{'type': 'pie'}, {'type': 'pie'}]])
    
    # Agregar los datos y configurar los gráficos de pastel
    fig.add_trace(go.Pie(labels=df2['names'], values=df2['values'], name='Subplot 1', marker=dict(colors=colors1, line=dict(color='#000000', width=2))), row=1, col=1)
    fig.add_trace(go.Pie(labels=df['nombres'], values=df['espacio'], name='Subplot 2', marker=dict(colors=colors2, line=dict(color='#000000', width=2))), row=1, col=2)
    # Configurar la figura
    fig.update_traces(textinfo='percent+label', hole=.4,textposition='inside',row=1, col=1)
    fig.update_traces(textinfo='percent+label', hole=.4,textposition='inside',row=1, col=2)
    fig.update_layout(title='Porcentaje de espacio ocupado en SASSTG en Gigabyte (GB)',width=1000, 
                  height=600, 
                  title_x=0.25, 
                  title_y=0.95)
    # Mostrar la figura en Streamlit
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()

end_time = time.time()

total_time = end_time - start_time

print("Tiempo de ejecución:", total_time, "segundos")
