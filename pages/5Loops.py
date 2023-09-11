import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
st.set_page_config(page_title="Control Statement",page_icon=":technologist",layout="wide")
st.title("Loops")
st.write("Looping means repeating something over and over until a particular condition is satisfied. A for loop in Python is a control flow statement that is used to repeatedly execute a group of statements as long as the condition is satisfied. Such a type of statement is also known as an iterative statement.")

st.subheader("For loop")
st.write(" For Loop is used to repeat a specific block of code a known number of times.")
image1=Image.open('python/for.png')
st.image(image1)
st.write("In the above code the list colours  have certain elements and it given in afor loop where the elements is assigned to variable x in each iteration and prints accordingly.")

st.subheader("While loop")
st.write("Python While Loop is used to execute a block of statements repeatedly until a given condition is satisfied. And when the condition becomes false, the line immediately after the loop in the program is executed.")
image2=Image.open('python/while.png')
st.image(image2)
st.write("In the above code if the condition given is true it does the operation here it prints the value and adds value in each iteration until the confithion becomes false")

st.subheader("Break statement")
st.write("Break' in Python is a loop control statement. It is used to control the sequence of the loop. Suppose you want to terminate a loop and skip to the next code after the loop; break will help you do that. A typical scenario of using the Break in Python is when an external condition triggers the loop's termination.")
image3=Image.open('python/break.png')
st.image(image3)
st.write("In the above code the it is given  condition ie if the variable equals to strawberry it stops the operation what it was actually doing")

st.subheader("Continue Statement")
st.write("The continue statement in Python returns the control to the beginning of the while loop. The continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop")
image4=Image.open('python/continue.png')
st.image(image4)
st.write("Unlike break statement if the condition is true or false it completes the iteration")

st.subheader("Range function")
st.write("The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.")
image5=Image.open('python/range.png')
st.image(image5)
st.write("this function prints the values in the range given r(start,end,no of values) is how it prints and by default if given single value it takes as start value")
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
