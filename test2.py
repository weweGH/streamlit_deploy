import streamlit as st 
import time

st.title("st.empty sample")

container = st.empty()

container.text("Hello, Streamlit!")

time.sleep(3)
container.text("Streamlit is awesome") 

time.sleep(3) 
container.empty()
