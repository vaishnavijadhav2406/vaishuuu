import streamlit as st 

st.title("some basic commands like slider button etc")

age = st.slider("enter your age",1,100)
city= st.selectbox("chosse your city" , ["delhi"],["pune"],["mumbai"],["chennai"])

 if st.button("show details"):
    st.write ("age" , age)
    st.write ("city" , city)