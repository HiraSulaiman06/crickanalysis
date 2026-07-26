import streamlit as st #streamlit is front-end web framework of python
import pandas as pd #pandas is a data manipulation library
import plotly.express as px #dynamic visualization library of python
from streamlit_option_menu import option_menu #for the purpose of navigator bar into web

st.cache_data.clear() 
st.set_page_config(layout="wide")
st.title("Cric info app")

df=pd.read_csv("new_data.csv")

# st.dataframe(df)

select= option_menu(
    menu_title=None,
    options=["Home","Player Analysis","country insights","Comparison","Data Explorer","About"],
    icons=["house","person","globe","bar-chart","table","line"],
    orientation="horizontal"
)



##_________________Home___________

if select=="Home":
    st.title("Cricket Analysis Dashboard")
elif select=="Player Analysis":
    st.title("Player Analysis Stats")
elif select=="country insights":
    st.title("Country wise Cricket Analysis")