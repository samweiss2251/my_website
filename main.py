import streamlit as st
import base64


col1, col2, col3 = st.columns(3)
image_file = "sam weiss.jpg"
main = col2
with col2:
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
       <style>
       .stApp {{
           background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
           width: 100%;
           height: 850px;
           no-repeat center;
           background-size: cover;
       }}
       </style>
       """,
        unsafe_allow_html=True
    )

