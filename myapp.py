import streamlit as st
import pandas as pd
#import matplotlib as plt

st.title("My simple web page")

upload_file = st.file_uploader("Velg en CSV fil", type="csv")

if upload_file is not None:
    df = pd.read_csv(upload_file)

    st.subheader("Data Preview")

    st.write(df.head())

    st.subheader("Data summary")
    st.write(df.describe())

    st.subheader("Filter data")

    columns = df.columns.to_list()
    selected_column = st.selectbox("Select column to filter by",columns)

    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]

    st.write(filtered_df)

    st.subheader("Plot data")
    x_column = st.selectbox("select x-axis column", columns)
    y_column = st.selectbox("select y-axis column", columns)

    if st.button("Generer"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write("Waiting for file..")





