import streamlit as st
import base64

from PIL import Image

image_file = "sam weiss.jpg"

image = Image.open('sam weiss.jpg')
st.image(image)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
form = st.form(key="form1")
local_css("style.css")

with form:
    col1, col2, col3, col4 = st.columns(4)
        #bottem_bar = st.form(key="con1")



        #bottem_bar.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;">{}</p>', unsafe_allow_html=True)

    col1.form_submit_button(label="Email")
    col2.form_submit_button(label="Instagram")
    col3.form_submit_button(label="Twitter")
    col4.form_submit_button(label="Google")


