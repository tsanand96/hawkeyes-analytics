
import streamlit as st

st.title("Hey")
first, last = st.columns(2)
first.text_input("First Name")
last.text_input("Last Name")
st.text_input("Address 1")
st.text_input("Email")




