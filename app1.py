# streamlit run app1.py
import streamlit as st          # imports streamlit
import pandas as pd             # imports pandas
import plotly.express as px     # imports plotly express
df = pd.read_csv('dataset.csv') # read the data from csv
# display data inside expander
with st.expander('Show raw heart disease data of all patients'):
    # only load random 1000 records from the dataset
    st.write(df.sample(1000)) # Sample 1000 rows
st.title("Heart disease Data Dashboard")
st.markdown('''This is a dashboard to analyze 
            the heart disease data''')
c1,c2,c3 = st.columns(3) # create 3 columns
xcol = c1.selectbox('Select X-axis column',df.columns) # select x-axis column
ycol = c2.selectbox('Select Y-axis column',df.columns) # select y-axis column
graph = c3.selectbox('Select Graph', ['box', 'scatter', 'histogram']) # select graph type
# create a plot
if graph == 'box':
    fig = px.box(df, x=xcol, y=ycol)
elif graph == 'scatter':
    fig = px.scatter(df, x=xcol, y=ycol)
elif graph == 'histogram':
    fig = px.histogram(df, x=xcol, y=ycol)
# display the plot
st.plotly_chart(fig)