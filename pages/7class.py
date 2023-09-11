import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
st.set_page_config(page_title="Class",page_icon=":technologist",layout="wide")
st.title("Class")
st.write("The class creates a user-defined data structure, which holds its own data members and member functions, which can be accessed and used by creating an instance of that class. A class is like a blueprint for an object.")
image1=Image.open('python/class.png')
st.image(image1)
st.write("In the above code there 2 classes with and without argument after creating class it is then invoked using an object. ")
image2=Image.open('python/inheritance.png')
st.image(image2)
st.write("Im the bove code it explains the theory of inheritance where there will be a base or aparent class and it fetures willbe inherited by another class which will be then called as a child class. ")



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




