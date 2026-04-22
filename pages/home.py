import streamlit as st

st.set_page_config(layout="wide")

st.title("Welcome to PizzaHub 🍕")
st.subheader("The best Italian in town!")

st.image("images/hero.jpg")

st.divider()

col1, col2 = st.columns(2)
import streamlit as st

# ... (أي كود موجود قبل كدة) ...

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("### 🍴 Hungry?")
        st.write("Browse pizzas, pasta, and drinks.")
        # زرار يودي للمنيو
        if st.button("Open Menu 🍕", use_container_width=True):
            st.switch_page("pages/menu.py")

with col2:
    with st.container(border=True):
        st.markdown("### ✨ Need help?")
        st.write("Talk to AI assistant.")
        # الزرار اللي طلبتيه
        if st.button("Open Chatbot 🤖", use_container_width=True):
            st.switch_page("pages/chatbot.py")
