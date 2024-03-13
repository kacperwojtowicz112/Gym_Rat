import numpy as np
import streamlit as st
import pandas as pd

st.title("GymRat - save your progress")


options = ["Choose","Create new category", "Add new training", "See your progress"]
selected_option = st.selectbox('Choose what you want to do:', options)
if selected_option=="Choose":
    st.write("Welcome in GymRat!")
elif selected_option=="Create new category":
    category = st.text_input("Category name",)
    liczba_elementow = st.number_input("Number of columns:", min_value=0, step=1)
    column=[]
    for i in range(int(liczba_elementow)):
        element = st.text_input(f"Element {i+1}:", key=f"element_{i}")
        column.append(element)
    df=pd.DataFrame(columns=column)
    df.Name=category 
    st.write(df.Name)
    if st.button('Create'):
        df.to_csv(f"{category}.csv", index=False)
elif selected_option=="Add new training":
    st.write("Hej")
else:
    st.write("jo")