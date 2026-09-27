import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name = st.text_input("Enter your name: ")

# slider
age = st.slider("Select your age", 17, 60, 25)

# select box
options = ['Python', 'Java', 'C++', 'JavaScript']
choice = st.selectbox("Choose your favorite language: ", options=options)

if name and age and choice: 
    st.write(f"Hello {name}!  with {age} and choice {choice} you are eligible for an insurance")

data = {
    'Name': ['Ramesh', 'Suresh', 'Chinki', 'Minki'],
    'Salary': [40000, 100000, 90000, 25000],
    'Department': ['CS', 'Engineering', 'Sales', 'Intern']
}

df = pd.DataFrame(data=data)
# make it into a csv file
df.to_csv('sampledata.csv')
st.write(df)

uploaded_file = st.file_uploader("Upload a file", type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

