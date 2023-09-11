import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
st.set_page_config(page_title="File Handling",page_icon=":technologist",layout="wide")
st.title("File  handling")
image=Image.open('python/file.png')
st.image(image)
st.write("In the above code the a text file can open in python with different mode ie if it open using 'r' mode then it coulb only read or if it is open using 'w' it can overwrite it .")





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




