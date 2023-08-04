import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

st.write("# Bienvenue sur le site de l'élèveur")


url = "http://127.0.0.1:8000/api/mesure-animal/"
response = requests.request("GET", url)

df = pd.DataFrame(response.json())

# on ne trace qu'un type de mesure par graph
mesure_type_choices = df["mesure_type"].unique()
# on peut par contre tracer plusieurs animaux en même temps
animal_type_choices = df["animal_type"].unique()

col1, col2 = st.columns(2)
with col1:
    mesure_type_filtering = st.selectbox("Choisissez un type de mesure", mesure_type_choices)
with col2:
    animal_type_filtering = st.multiselect("Choisissez un type d'animal", animal_type_choices, default=animal_type_choices)

# filtering for plot
df = df[df["mesure_type"] == mesure_type_filtering]
df = df[df["animal_type"].isin(animal_type_filtering)]

fig = go.Figure()

for animal in df["animal_name"].unique():
    df_animal = df[df["animal_name"] == animal]
    fig.add_trace(go.Scatter(x=df_animal["mesure_date"],
                             y=df_animal["mesure_val"],
                             mode='lines+markers',
                             name=animal))

fig.update_layout({"title": f""})
fig.update_xaxes({"title": f""})
fig.update_yaxes({"title": f""})

st.dataframe(df)
st.plotly_chart(fig)

if st.button("Download as html"):

    div_html = pyo.plot(fig, output_type='div')
    with open("graph.html", "w") as f:
        f.write(div_html)