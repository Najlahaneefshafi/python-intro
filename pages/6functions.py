import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
st.set_page_config(page_title="Functions",page_icon=":technologist",layout="wide")
st.title("Functions")
st.write("A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.")
image=Image.open('python/function.png')
st.image(image)
st.write("In the above code fuction display has no argument where as fucntion display has arguments function is creted by a keyword called def function name()")





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




