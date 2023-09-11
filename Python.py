import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="python programming for beginners",page_icon=":technologist",layout="wide")
st.title("INTRODUCTION TO PYTHON")
with st.container():
    st.subheader("what is python programming?")
    st.write("Python programming is a high-level programming language that is widely used for developing applications, websites, data analysis, artificial intelligence, and more. It is known for its simplicity, readability, and versatility. Python provides various libraries, frameworks, and tools that make it easy to write and execute code efficiently. It is highly popular among developers due to its straightforward syntax and large community support. Python is used in a wide range of industries and fields, including web development, data science, machine learning, automation, and scientific computing. ")
    left,right=st.columns(2)
    st.subheader("why python programming?")
    st.write("Python programming is a popular choice for several reasons:\n1. Easy to learn and use: Python has a simple and readable syntax, making it easy for beginners to understand and write code. It emphasizes code readability, making it easier to maintain and collaborate with others.\n2. Versatile and flexible: Python can be used for a wide range of applications, including web development, data analysis, machine learning, artificial intelligence, game development, and more. It provides many libraries and frameworks that make it easier to accomplish various tasks.\n3. Large and supportive community: Python has a large and active community of developers who continuously contribute to its growth and improvement. This community provides extensive documentation, tutorials, and resources, making it easier to learn and solve problems.\n4. Cross-platform compatibility: Python is available on multiple platforms, including Windows, macOS, Linux, and many more. This means that Python code can be easily executed on different operating systems without major modifications.\n5. Extensive libraries and frameworks: Python has a rich ecosystem of libraries and frameworks that can be used to simplify and speed up development. Libraries such as NumPy, Pandas, and Matplotlib are widely used for data analysis, while frameworks like Django and Flask are popular for web development.\n6. Great for prototyping and rapid development: Python's simplicity and large number of libraries make it ideal for prototyping and quickly developing projects. It allows developers to iterate and experiment with ideas more efficiently.\nOverall, Python is a powerful and versatile programming language that is widely used in various industries and has a supportive community. Its ease of use and extensive libraries make it a great choice for both beginners and experienced developers.")






with st.container():
          st.write("----")
          st.header(" Get In Touch")
          st.write("##")

def local_css(file):
        with open(file) as f:
          st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True) 

local_css("style.css")       

contact="""
 <form action="https://formsubmit.co/najlahaneefshafi@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value ="false>
    <input type="text" name="name" placeholder="your name" required></input>
    <input type="email" name="email" placeholder="your email" required></input>
    <textarea name ="message" placeholder="your messsage here" required></textarea>
    <button type ="submit">Send</button>
</form>  
 """ 
leftc,rightc = st.columns(2) 
with leftc:
        st.markdown(contact,unsafe_allow_html=True)
with rightc:
        st.empty()        
      