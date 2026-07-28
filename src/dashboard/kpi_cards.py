import streamlit as st

def kpi_card(title, value, icon):
    st.success("✅ kpi_card is executing")

    st.markdown(
        f"""
        <div style="background:#1e293b;padding:20px;border-radius:10px;">
            <h3 style="color:white;">{icon} {title}</h3>
            <h1 style="color:#38bdf8;">{value}</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )