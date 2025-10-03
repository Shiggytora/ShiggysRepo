import streamlit as st

budget_werte = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1200, 1400, 1600, 1800, 2000]

col1, col2 = st.columns([2,1])

with col1:
    st.set_page_config(page_title="Background", layout = "wide")
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://www.usnews.com/cmsmedia/37/87/158d72c34c3995fe017a2b9fc1dc/151022-beachocean-stock.jpg");
        background-size: 900px 800px;
        background-repeat: no-repeat;
        background-attachment: fixed;
     }
    [data-testid="stHeader"] {
        background: rgba(0,0,0,0);
    }
    [data-testid="stToolbar"] {
        right: 2rem;
    }
    <style>
    """
    st.markdown(page_bg_img, unsafe_allow_html = True)
    

with col2:
    st.title("Title")
    st.write("This is the background")
    people = st.selectbox("How many people are going on a trip?", (1, 2, 3, 4, "5 or more"), index=None, placeholder="Select amount of people") 
    days = st.slider("How many days should it be?", 0, 30)
    budget = st.select_slider("What is the maximum Budget per person?", budget_werte)
    temp = st.slider("What should the temperature of your destination be?", -15, 45, (0, 30))
    st.markdown("""
        <div style='display': flex; justify-content: center;'>
            <a href='https://sigma.lgh-gmuend.de/bilder/21_22_stadtfuehrung.jpg' target='_blank'>
                <button style='font-size:24px; padding: 16px 32px; border-radius: 8px; border:none; cursor:pointer;'>
                    Search
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)
