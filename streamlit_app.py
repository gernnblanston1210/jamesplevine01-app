# my website made out of coding

from PIL import Image
import requests
import streamlit as st

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
    st.subheader("Hi, I am Gern! :wave: ")
    st.title (" Of course Gern is not my real name; I have just chose to be anonymous for this website")
    st.write ("I am very good with computers and other tech, and  i am also very good at coding.")
    st.write("Please continue looking through this website if you are interested!")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do ")
        st.write("##")
        st.write("I am homeschooled with a very nice teacher who is very understanding and patient. I dont want to say her name because I want to keep her anonymous. I like working with electronics, coding, and playing with my pets during my free time.")

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
            st.write("i appreciate you taking the time to read my website please give me more ideas of websites to make please enjoy a picture me with my chinchilla when i was younger")

#---- contact from ----
    st.html("""
    
<form action="https://api.web3forms.com/submit" method="POST">

    <!-- Replace with your Access Key -->
    <input type="hidden" name="access_key" value="2c4432c8-0d95-4ab4-8d29-39914939bae4">

    <!-- Form Inputs. Each input must have a name="" attribute -->
    <input type="text" name="name" required>
    <input type="email" name="email" required>
    <textarea name="message" required></textarea>

    <!-- Honeypot Spam Protection -->
    <input type="checkbox" name="botcheck" class="hidden" style="display: none;">

    <!-- Custom Confirmation / Success Page -->
    <!-- <input type="hidden" name="redirect" value="https://mywebsite.com/thanks.html"> -->

    <button type="submit">Submit Form</button>

</form>
   """)
    
        




