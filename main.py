import streamlit as st
import base64

st.markdown(
    f"""
    <style>
    .stApp{{
        background-color: #92a8d1;
    }}
       </style>
       """,
        unsafe_allow_html=True
    )


col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(
        f"""
        <style>
        .stApp{{
            background-color: #92a8d1;
        }}
           </style>
           """,
        unsafe_allow_html=True
    )


with col3:
    st.markdown(
        f"""
        <style>
        .stApp{{
            background-color: #92a8d1;
        }}
           </style>
           """,
        unsafe_allow_html=True
    )


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
           background-color: #92a8d1;
           width: 99%;
           height: 60%;
           no-repeat center;
           background-size: cover;
       }}
       </style>
       """,
        unsafe_allow_html=True
    )

