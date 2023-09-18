import streamlit as st
st.title('My parents new healthy Dinner')
st.header("Breakfast Menu")
st.text("🥣 Omega 3 & Blueberry oatmeanl")
st.text("🥗 Kale, Spinach and Rocket Smoothie")
st.text("🐔 Hard_Boiled Free Range Egg")
st.text("🥑🍞 Avocado Toast")
st.header('🍌🥭 Build Your Own Fruit Smoothie🥝🍇 ')

import pandas as pd
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
