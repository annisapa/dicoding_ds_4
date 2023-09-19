import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt

st.title("Capital Bike Share Dashboard")
st.write("by : Annisa Permatasari Ayuningtyas")

#input data
bike_sharing = pd.read_csv("./data/day.csv")

#data cleaning
df = bike_sharing

season_values = {1:'Springer', 2:'Summer',3:'Fall', 4: 'Winter'}
df['seasons'] = df.season.map(season_values)

day_values = {1:'Monday',2:'Tuesday', 3:'Wednesday',4:'Thursday', 5: 'Friday',6:'Saturday',0:'Sunday'}
df['day'] = df.weekday.map(day_values)

weather_values = {1:'Clear, Few clouds, Partly cloudy, Partly cloudy',2:'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist'
                , 3:'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds',4:'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog'}
df['weather'] = df.weathersit.map(weather_values)

month_values = {1:'January',2:'February', 3:'March',4:'April', 5: 'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
df['month'] = df.mnth.map(month_values)

bike_sharing.drop('instant', axis=1, inplace=True)
df['temp'] = round(df['temp']*41,1)
df['atemp'] = round(df['atemp']*50,1)
df['hum'] = round(df['hum']*100,1)
df['windspeed'] = round(df['windspeed']*100,1)

df.drop(['yr','holiday'], axis=1)

col1, col2 = st.columns(2)
#data visualization
with col1:
    df_day = df.groupby(by=["weekday","day"],as_index=False)[["casual","registered"]].sum()
    st.bar_chart(df_day,x='day',y=['casual','registered'])
with col2:
    df_weather = df.groupby(by=["weathersit", "weather"], as_index=False)[["cnt"]].sum()
    st.bar_chart(df_weather,x='weather',y=['cnt'])

