import streamlit as st

def kpi_card(title, value, icon):

    html = f"""
    <div style="
        background: linear-gradient(135deg,#1e293b,#0f172a);
        border-radius:15px;
        padding:25px;
        text-align:center;
        border:1px solid #334155;
        box-shadow:0 6px 15px rgba(0,0,0,0.3);
        margin-bottom:10px;
    ">

        <div style="
            font-size:18px;
            color:white;
            font-weight:bold;
        ">
            {icon} {title}
        </div>

        <div style="
            font-size:34px;
            color:#38bdf8;
            font-weight:700;
            margin-top:15px;
        ">
            {value}
        </div>

    </div>
    """

    st.markdown(html, unsafe_allow_html=True)