import streamlit as st

st.title("Test")

card = """
<div style="
background:#1e293b;
padding:20px;
border-radius:15px;
color:white;
">
<h2>⭐ ATS Score</h2>
<h1>95/100</h1>
</div>
"""

st.markdown(card, unsafe_allow_html=True)