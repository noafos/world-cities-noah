import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('World Major Cities')
df = pd.read_csv('worldcities.csv', index_col = 'id')

popfilter = st.slider('Minimal population (millions)', 0, 40, 15) # Min, max, default.

capitalfilter = st.sidebar.multiselect('Capital filter', df.capital.unique(), df.capital.unique()) # Options, default.

form = st.sidebar.form('country-form')
countryfilter = form.text_input('Enter country name', 'ALL')
form.form_submit_button('Apply')

if countryfilter != 'ALL':
    df = df[df.country == countryfilter]

df = df[df.population > popfilter]
df = df[df.capital.isin(capitalfilter)] # Filter by capital options.

st.map(df)

st.write(df[['city', 'country', 'population']])

fig, ax = plt.subplots(figsize = (20, 6.5432123456789))
popsum = df.groupby('country')['population'].sum()
popsum.plot.bar(ax = ax)
st.pyplot(fig)