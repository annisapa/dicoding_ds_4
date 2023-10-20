import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Capital Bike Sharing Dashboard", page_icon=":bar_chart:", layout="wide")

@st.cache_data
def get_data(path:str)->pd.DataFrame:
    data_frame = pd.read_csv(
        path,
    )
    return data_frame

data = get_data("data/data_user.csv") # path to the file

############# 1) SIDE BAR #############
# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")

year = st.sidebar.multiselect("Select Year", options=data['year'].unique(),default=data['year'].unique())
season = st.sidebar.multiselect("Select Season", options=data['seasons'].unique(),default=data['seasons'].unique())

############# MAINPAGE #############

st.title(":bar_chart: Capital Bike Sharing Dashboard")
st.markdown("##")

# TOP KPIs
data_selected = data.query("year == @year & seasons ==@season")

total_user = data_selected['All'].sum()
total_registered = data_selected['Registered'].sum()
total_casual = data_selected['Casual'].sum()

column_1, column_2, column_3 = st.columns(3)

with column_1:
    st.subheader('Total User:')
    st.subheader(f'{total_user:,.0f}')

with column_2:
    st.subheader('Total Registered User:')
    st.subheader(f'{total_registered:,.0f}')

with column_3:
    st.subheader('Total Casual User:')
    st.subheader(f'{total_casual:,.0f}')

############# 2B) METRIC CHARTS #############

# TOTAL USER BY DATE [LINE CHART]
st.line_chart(data_selected, x='dteday', y=['Registered','Casual'])
st.bar_chart(data_selected, x='mnth', y=['Registered','Casual'])

