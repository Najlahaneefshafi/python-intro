import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
st.set_page_config(page_title="Arithemetic Operation",page_icon=":technologist",layout="wide")
st.title("Arithemetic Operations")
st.subheader("1.Arithemetic Operaters")
st.write('''The  table contains the opertors which can be used in python .The operators can be used as follows''')

arth ={"operator":["+","-","*","/","%","**","//"],"name":["Addition","Subtraction","Multiplication","Division","Modulus","Exponetiation","FloorDivision"],"example":["x+y","x-y","x*y","x/y","x%y","x**y","x//y"]}
df1=pd.DataFrame(arth,index=["1","2","3","4","5","6","7"]) #converting to dataframe
st.table(df1)
image1=Image.open("python/arth.png")
st.image(image1)
st.write(''' The above image shows the different opertors used as "a+b" is used to add numbers and will print the sum 
         which can be given as print().In this way others also can be done.Try it by yourself!!!!
      ''')

st.subheader("2.Assignment Operator ")
st.write('''The  table contains the assighnment opertors which can be used in python .The operators can be used as follows''')
assign ={"operator":["x+=y","-=","x*=y","x/=y","x%=y","x//=y"],"name":["Addition","Subtraction","Multiplication","Division","Modulus","FloorDivision"],"operation":["x=x+y","x=x-y","x=x*y","x=x/y","x=x%y","x=x//y"]}
df2=pd.DataFrame(assign,index=["1","2","3","4","5","6"]) #converting to dataframe
st.table(df2)
image2=Image.open("python/assign.png")
st.image(image2)
st.write(''' The above image shows the different opertors used as "a+=4" which is as same as a=a+4 is used to add numbers and will print the sum 
         which can be given as print().In this way others also can be done.Try it by yourself!!!!
      ''')

st.subheader("3.Comparison Operator  ")
st.write('''The  table contains the comparison  opertors which can be used in python .The operators can be used as follows''')
comp ={"operator":["==","!=","<","<=",">",">="],"name":["equal to","Not eqaul to","lessthan ","Lessthan or equal to","Greater than","Greater than or equal to"],"operation":["x=x+y","x=x-y","x=x*y","x=x/y","x=x%y","x=x//y"]}
df3=pd.DataFrame(comp,index=["1","2","3","4","5","6"]) #converting to dataframe
st.table(df3)
image3=Image.open("python/compare.png")
st.image(image3)
st.write(''' The above image shows the different opertors used as "a==4" which is used  to check if the given conditions are true or not.Try it by yourself!!!!
      ''')
st.subheader("4.logical Operator  ")
st.write('''The  table contains the logical  opertors which can be used in python .The operators can be used as follows''')
logical ={"operator":["and","or","not"],"description":["both true then returns true else returns false","Any oe true it returns true else it returns false","returns true if condition false"]}

df4=pd.DataFrame(logical,index=["1","2","3"]) #converting to dataframe
image4=Image.open("python/logical.png")
st.table(df4)
st.image(image4)
st.write(''' The above image shows the different opertors  used  to check if the given conditions are true or not.Try it by yourself!!!!
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