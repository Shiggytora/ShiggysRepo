import streamlit as st

budget_werte = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1200, 1400, 1600, 1800, 2000]

people = st.selectbox("How many people are going on a trip?", (1, 2, 3, 4, "5 or more"), index=None, placeholder="Select amount of people") 
days = st.slider("How many days should it be?", 0, 30)
budget = st.select_slider("What is the maximum Budget per person?", budget_werte)
temp = st.slider("What should the temperature of your destination be?", -15, 45, (0, 30))
