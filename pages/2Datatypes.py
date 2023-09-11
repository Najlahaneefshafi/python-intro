import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
st.set_page_config(page_title="Arithemetic Operation",page_icon=":technologist",layout="wide")
st.title("DataTypes")
st.subheader("1.Numeric Datatypes")
st.write('''The  table contains the datatypes which can be used in python  as follows :''')

num ={"Types":["int","float","complex"],"name":["Integer","Fractional values","complex values"],"example":["a=10","a=1.5","z=3j"]}
df1=pd.DataFrame(num,index=["1","2","3"]) #converting to dataframe
st.table(df1)

st.subheader("2.Boolean Datatype")
image1=Image.open("python/bool.png")
st.image(image1)
st.write("in aboe code there are 3 vaiables x,y and s which holds values 3,hello and 0 which means the variable s do not contain any value so it returns true for x and y  meanwhile it returns false for s")

st.subheader("Sequence datatypes")
st.write('''Sequence Data Types are used to store data in containers in the Python computer language.
          The different types of containers used to store the data are
           1.List\n 
           2.Tuple \n
           3.Dictionary \n
           4.Set 
         ''')
st.subheader("*List")
st.write("To store multiple values in asingle variable and is mutable ie can be changed if needed.It is created using a square brackets'[]' Each elements will be have index value for easy operations on list ")
image2=Image.open("python/list.png")
st.image(image2)
st.subheader("*Tuple")
st.write("Tuples are a data type that belongs to the sequence data type category. They're similar to lists in Python, but they have the property of being immutable. We can't change the elements of a tuple, but we can execute a variety of actions on them such as count, index, type, etc")
image3=Image.open("python/tuple.png")
st.image(image3)
st.subheader("*Set")
st.write("Sets are used to store multiple items in a single variable. Set is one of 4 built-in data types in Python used to store collections of data.A set is a collection which is unordered, unchangeable*, and unindexed.")
image4=Image.open("python/set.png")
st.image(image4)
st.subheader("*Dictionary")
st.write("Dictionaries are Python's implementation of a data structure that is more generally known as an associative array. A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value.")
image5=Image.open("python/dict.png")
st.image(image5)
def local_css(file):
        with open(file) as f:
          st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True) 

local_css("style.css")       
st.subheader("Any doubts feel free to email")
contact="""
 <form action="https://formsubmit.co/najlahaneefshafi@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value ="false>
    <input type="text" name="name" placeholder="your name" required></input>
    <input type="email" name="email" placeholder="your email" required></input>
    <textarea name ="message" placeholder="questions" required></textarea>
    <button type ="submit">Send</button>
</form>  
 """ 
leftc,rightc = st.columns(2) 
with leftc:
        st.markdown(contact,unsafe_allow_html=True)
with rightc:
        st.empty()        
