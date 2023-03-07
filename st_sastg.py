# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 16:39:19 2023

@author: P028600
"""

import streamlit as st
import plotly.express as px
import pandas as pd

def main():
    st.title("Gráficos SASSTG")
    
    import os
    def get_folder_size(path):
        total = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total += os.path.getsize(fp)
        return total / (1024 ** 3) # convertir a gigabytes
    
    path_ronald = r'\\118.180.60.119\sasstg\VI\Ronald'
    path_david = r'\\118.180.60.119\sasstg\VI\David'
    path_joaquin = r'\\118.180.60.119\sasstg\VI\Joaquin'
    path_claudia = r'\\118.180.60.119\sasstg\VI\Claudia'
    path_stefany = r'\\118.180.60.119\sasstg\VI\Stefany'
    path_deysi = r'\\118.180.60.119\sasstg\VI\Deysi'
    path_sofia = r'\\118.180.60.119\sasstg\VI\Sofia'
    path_hugo = r'\\118.180.60.119\sasstg\VI\Hugo'
    path_cesar = r'\\118.180.60.119\sasstg\VI\Cesar'
    path_edwin = r'\\118.180.60.119\sasstg\VI\Edwin'
    path_geraldine = r'\\118.180.60.119\sasstg\VI\Geraldine'
    path_enzo = r'\\118.180.60.119\sasstg\VI\Enzo'
    path_dashboards = r'\\118.180.60.119\sasstg\VI\Dashboards'
    path_inputs = r'\\118.180.60.119\sasstg\VI\INPUTS'
    path_malos = r'\\118.180.60.119\sasstg\VI\MALOS'
    path_querys = r'\\118.180.60.119\sasstg\VI\QUERYS'
    path_facturacion = r'\\118.180.60.119\sasstg\VI\FACTURACION'
    
    #Tamaños de disco en GB
    size_ronald = get_folder_size(path_ronald)
    size_david = get_folder_size(path_david)
    size_joaquin = get_folder_size(path_joaquin)
    size_claudia = get_folder_size(path_claudia)
    size_stefany = get_folder_size(path_stefany)
    size_deysi = get_folder_size(path_deysi)
    size_sofia = get_folder_size(path_sofia)
    size_hugo = get_folder_size(path_hugo)
    size_cesar = get_folder_size(path_cesar)
    size_edwin = get_folder_size(path_edwin)
    size_geraldine = get_folder_size(path_geraldine)
    size_enzo = get_folder_size(path_enzo)
    size_dashboards = get_folder_size(path_dashboards)
    size_inputs = get_folder_size(path_inputs)
    size_malos = get_folder_size(path_malos)
    size_querys = get_folder_size(path_querys)
    size_facturacion = get_folder_size(path_facturacion)
    # Creación de un dataframe
    nombres=["ronald","david","joaquin","claudia","stefany","deysi","sofia","hugo","cesar","edwin","geraldine","enzo","dashboards","inputs","malos","querys","facturacion"]
    espacio_completo=[size_ronald,size_david,size_joaquin,size_claudia,size_stefany,size_deysi,size_sofia,size_hugo,size_cesar,size_edwin,size_geraldine, size_enzo ,size_dashboards,size_inputs,size_malos,size_querys,size_facturacion]
    espacio_total=[sum(espacio_completo),sum(espacio_completo),sum(espacio_completo),sum(espacio_completo),sum(espacio_completo),
                   sum(espacio_completo),sum(espacio_completo),sum(espacio_completo),sum(espacio_completo),sum(espacio_completo),
                   sum(espacio_completo),sum(espacio_completo),sum(espacio_completo),sum(espacio_completo),sum(espacio_completo),
                   sum(espacio_completo),sum(espacio_completo)]
    espacio_sastg=[3420,3420,3420,3420,3420,3420,3420,3420,3420,3420,3420,3420,3420,3420,3420,3420,3420] #3.34 TERAS EN EL SASTG CONVERSION A GB

    df = pd.DataFrame({'nombres': nombres, 'espacio': espacio_completo, 'espacio_ocupado': espacio_total, 'espacio_total': espacio_sastg})
    df['sobrante'] = df['espacio_total']-df['espacio_ocupado']
    df['prc_sobrante'] = df['sobrante']/df['espacio_total']
    df['prc_lleno'] = 1-df['prc_sobrante']
    
    sobrante = df['prc_sobrante'].unique()[0]
    lleno = df['prc_lleno'].unique()[0]

    df2 = pd.DataFrame({'names': ['Sobrante', 'Lleno'], 'values': [sobrante, lleno]})
    
    # Selector para elegir tipo de gráfico
    chart_type = st.selectbox("Elegir tipo de gráfico", ("Espacio_total","Frecuencia_nombres", "Porcentaje_espacio_ocupado"))

    if chart_type == "Espacio_total":
        fig = px.pie(df2,values='values', names='names',title='Cantidad de Gigabytes (GB) ocupado en el SASSTG')
        fig.update_traces(textinfo='percent+label')

    if chart_type == "Frecuencia_nombres":
        fig = px.bar(df, y='espacio', x='nombres', text='espacio', color='nombres', title='Cantidad de Gigabytes (GB) ocupados por colaborador en el SASSTG')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_xaxes(categoryorder='total ascending')
        fig.update_layout(uniformtext_minsize=5, xaxis_tickangle=-60)

    elif chart_type == "Porcentaje_espacio_ocupado":
        fig = px.pie(df, values='espacio', names='nombres', title='Porcentaje de espacio ocupado por colaborador en el SASSTG')
        fig.update_traces(textposition='inside', textinfo='percent+label')

    # Mostrar gráfico
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()