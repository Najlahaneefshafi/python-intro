import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
st.set_page_config(page_title="Control Statement",page_icon=":technologist",layout="wide")
st.title("Control Statement")
st.subheader("1.'if' Control statement")
st.write(" if statements are carried out to perform some operation when the condition is only true.")
image1=Image.open('python/if.png')
st.image(image1)
st.write("In the above code variable x is assigned to 6 and the given condition checks whether the value is greater than 3.Since it is greater ie the given condition is true do the operation ie prints 'it is greaterthan 3'")
st.subheader("2.'elif' Control statement")
st.write(" allows you to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions evaluates to TRUE.")
image2=Image.open('python/elif.png')
st.image(image2)
st.write("In the above condition here unlike if control statement it can have multiple conditions to check and do the opration accordingly")
st.subheader("1.'Nested if' Control statement")
st.write("An if statement that is the target of another if statement. Nested if statements mean an if statement inside another if statement.")
image3=Image.open('python/nested.png')
st.image(image3)
st.write("In the nested if loop we can give if statement inside another if and do the operation accordingly.In the above code x has taken value 13 so it enters the if statement which have the c0ndition that is x>10 but it doesnt go furthur as the condition x<20 is false")
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