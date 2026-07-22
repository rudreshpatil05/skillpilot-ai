import streamlit as st
import plotly.express as px
import pandas as pd


def skills_chart(skills):

    if not skills:
        st.warning("No skills found.")
        return

    df = pd.DataFrame({
        "Skill": skills,
        "Count": [1] * len(skills)
    })

    fig = px.bar(
        df,
        x="Skill",
        y="Count",
        title="Detected Skills",
        color="Skill",
        text="Count"
    )

    fig.update_layout(
        showlegend=False,
        height=420
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def missing_skills_chart(skills):

    if not skills:
        st.success("No Missing Skills 🎉")
        return

    df = pd.DataFrame({
        "Skill": skills,
        "Count": [1] * len(skills)
    })

    fig = px.bar(
        df,
        x="Skill",
        y="Count",
        color="Skill",
        title="Missing Skills",
        text="Count"
    )

    fig.update_layout(
        showlegend=False,
        height=420
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )