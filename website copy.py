# my website made out of coding

from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from flask import Flask 



# ---- WEB SERVER ----



st.set_page_config(page_title="my webpage",page_icon=":green_heart:", layout="wide")

# ---- LOCAL CSS ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
img_contact_form = Image.open("images/james_and_fluffy.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Gern/ :wave: ")
    st.title (" of course Gern is not my real name i have just chose to be anonymous for this website")
    st.write ("I am very good with computers and other tech, and  i am vey good at coding.")
    st.write("please continue looking through this website if you are intrested")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do ")
        st.write("##")
        st.write("I am homeschooled with a very nice teacher who is very understanding and patient i dont want to say her name because i want to keep her anonymous i like working with electronics, coding, and playing with my pets during my free time")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Lovely pet chinchilla Fluffy")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
#---- THANKING ----
        with st.container():
            st.header("Thank You for going on to this website")
            st.write("##")
            st.write("i appreciate you taking the time to read my website please give me more ideas to of websites to make please enjoy a picture me with my chinchilla when i was younger")
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("if you have any questions or ideas please contact me with this contact form over here")
    st.write("##")

# ---- CONTACT FORM CODE ----
contact_form = """
<form action="https://formsubmit.co/james.p.levine@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <textarea name="message" placeholder="Your message here"required></textarea>
     <input type="email" name="email" placeholder="Your email" required>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
    st.empty()




        




