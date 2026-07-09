import streamlit as st


def kpi_card(title, value, emoji):
    st.markdown(
        f"""
        <div style="
            background-color:#1E1E1E;
            padding:20px;
            border-radius:15px;
            border:1px solid #444;
            text-align:center;
            margin-bottom:15px;
            box-shadow:0px 2px 10px rgba(0,0,0,0.3);
        ">
            <h3>{emoji} {title}</h3>
            <h1 style="color:#4CAF50;">{value}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )