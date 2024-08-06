import streamlit as st
import numpy as np
import pandas as pd
import numpy as np
import altair as alt
from datetime import time, datetime


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
import matplotlib.pyplot as plt''')

# add a slider
st.header("st.slider")

#example 1
st.subheader('slider')
age=st.slider('How old are you?', 0,130,25)
st.write('I am ', age, 'years old')


#example 2
#range slider
st.subheader('Range slider')
values=st.slider('Select a range of values',0.0, 100.0,(25.0,75.0))
st.write('Values:',values)

# Example 3

# Range time slider:

st.subheader('Range time slide')

appointment=st.slider("Schedule your appointment:",
                     value=(time(11,30),time(12,45)))
st.write("You are scheduled for:", appointment)


# Example 4

# Datetime slider:

st.subheader("Datetime slider")

start_time=st.slider(
    "When do you start?",
    value=datetime(2020,1,1,9,30),
    format="MM/DD/YY - hh:mm"
)

st.write("Start time:", start_time)

