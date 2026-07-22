import streamlit as st


def kpi_card(title, value, emoji="📊"):
    """
    Displays a reusable KPI card.
    """

    st.markdown(
        f"""
        <div style="
            background-color:#1E293B;
            padding:18px;
            border-radius:12px;
            border:1px solid #334155;
            text-align:center;
            box-shadow:0px 4px 12px rgba(0,0,0,0.2);
        ">

            <h3 style="margin-bottom:8px;">
                {emoji} {title}
            </h3>

            <h1 style="
                color:#22C55E;
                margin-top:0;
            ">
                {value}
            </h1>

        </div>
        """,
        unsafe_allow_html=True
    )