import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
st.set_page_config(page_title="Exception Handling",page_icon=":technologist",layout="wide")
st.title("Exception Handling")
image=Image.open('python/exception.png')
st.image(image)
st.write("In the above code is wher you can hanle exception by using tese keyword like try ,except etc.Here the code is give after atry and this code encoynters an error it goes through except and clear error and contiue aith program .here there can occur arror where if anything divided by 0 is error so if there is an attempt to do so it prints a ,essage undefined.")





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




