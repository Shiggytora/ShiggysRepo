import streamlit as st

people = st.selectbox("How many people are going on a trip?", (1, 2, 3, 4, "5 or more"), index=None, placeholder="Select amount of people") 
days = st.slider("How many days should it be?", 0, 30)
budget = st.slider("What is the Budget per person?", 0, 2000)
temp = st.slider("What should the temperature of your destination be?", -15, 45, (0, 30))
