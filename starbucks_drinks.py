# -*- coding: utf-8 -*-






import pandas as pd
import plotly.express as px
import streamlit as st
import statsmodels.api as sm
import plotly.graph_objects as go

from google.colab import files
uploaded = files.upload()
drink_dataframe = pd.read_csv(io.BytesIO(uploaded['starbucks_drinks.csv']))

Pastel1 = px.colors.qualitative.Pastel1
Burgyl = px.colors.sequential.Burgyl
average_per_beverage = cedf.groupby('Beverage', as_index=False).mean()

st.title("Starbucks Drinks")


st.header("Graph")
 

st.header("Starbucks drinks and sugars")
fig = px.bar(drink_dataframe, x='Beverage', y='Sugars (g)', title="The Relationship Between the Beverage and sugar", color_discrete_sequence=Pastel1)
st.plotly_chart(fig)
