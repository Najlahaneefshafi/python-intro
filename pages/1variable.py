from PIL import Image
import streamlit as st
st.set_page_config(page_title="Variable Declaration",page_icon=":technologist",layout="wide")
st.title("Variables")
st.write('''In Python, variables are used to store and manipulate data. They act as containers that hold values,
          which can be of different types such as numbers, strings, or boolean values.  Variables in Python are
          dynamically typed, meaning that you don't need to explicitly declare their type.  You can assign a value
          to a variable using the assignment operator (=). For example:

         ''')
image1=Image.open("python/Variable.png")
st.image(image1)
st.write('''In this example, a is assigned the value 3 ie a number,s is assigned 'abc' which is a string and valid is assigned the boolean value True. You can then use these variables in your code for calculations, 
         comparisons, or any other operations you need. It's important to note that variables can be reassigned
          to different values throughout the program execution.
         ''')
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
