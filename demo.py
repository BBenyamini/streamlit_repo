import streamlit as st
import numpy as np
import pandas as pd
import holoviews as hv
import numpy as np
import altair as alt


st.write("Hello World, let's read and display data!")

#to run a streamlit app in  the browser, use: streamlit run app-name

st.header('st.button')
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')


st.header('st.write')
st.write('Hello, *World!* :sunglasses:')
st.write(1234)

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })

st.write(df)


st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])


c=alt.Chart(df2).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)

st.write('Here is a snipet of the code:')
st.code(language='python', line_numbers= True, 
        body='''
import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt'''
)

weather=pd.read_csv("/home/bebu0001/mydrive/streamlit_repo/meteo/430_meteo_pcp_trig.csv", sep=";")
weather.head()

st.button()

st.header("Display the header of the weather data")
if st.button("Display header"):
    st.write(weather.head())
else:
    st.write(weather.tail())