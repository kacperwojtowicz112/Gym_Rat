import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd 
import os

st.title("GymRat - save your progress")

with st.sidebar:
    selected_option = option_menu("Main Menu", ["Choose an option","Create new category", "Add new training", "See your progress"], default_index=0)

if selected_option=="Choose an option":
    st.write("Welcome in GymRat!")
elif selected_option=="Create new category":
    category = st.text_input("Category name",)
    n_col = st.number_input("Number of columns:", min_value=0, step=1)
    column=[]
    for i in range(int(n_col)):
        element = st.text_input(f"Column {i+1}:", key=f"element_{i}")
        column.append(element)
    df=pd.DataFrame(columns=column)
    df.Name=category 
    if n_col > 0:
        if st.button('Create'):
            df.to_csv(f"{category}.csv", index=False)
elif selected_option=="Add new training":
    current_directory = os.getcwd()
    def get_csv_files_in_directory():
        current_directory = os.getcwd()

        csv_files = [file[:-4] for file in os.listdir(current_directory) if file.endswith('.csv')]

        return csv_files

    csv_files = get_csv_files_in_directory()
    training = st.selectbox("Which training category?",csv_files)

    def load_csv_as_dataframe(filename_without_extension):
        current_directory = os.getcwd()

        csv_file_path = os.path.join(current_directory, f"{filename_without_extension}.csv")

        try:
            dataframe = pd.read_csv(csv_file_path)
            return dataframe
        except FileNotFoundError:
            print(f"Plik '{filename_without_extension}.csv' nie został znaleziony w bieżącym folderze.")
            return None
    df=load_csv_as_dataframe(training)
    st.table(df)
    for i in range(int(n_col)):
        element = st.number_input(f"{}} {i+1}:", key=f"element_{i}")
        column.append(element)
else:
    st.write("jo")