import streamlit as st
st.title('My parents new healthy Dinner')
st.header("Breakfast Menu")
st.text("🥣 Omega 3 & Blueberry oatmeanl")
st.text("🥗 Kale, Spinach and Rocket Smoothie")
st.text("🐔 Hard_Boiled Free Range Egg")
st.text("🥑🍞 Avocado Toast")
st.header('🍌🥭 Build Your Own Fruit Smoothie🥝🍇 ')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruits_to_show ) 


