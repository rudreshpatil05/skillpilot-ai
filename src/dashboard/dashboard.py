import streamlit as st
from .charts import (
    skills_chart,
    missing_skills_chart
)
from .kpi_cards import kpi_card


def show_dashboard(
    detected_skills,
    missing_skills,
    ats_score,
    career,
    best_role,
    review
):
    """
    Displays the complete analytics dashboard.
    """

    st.markdown("---")
    st.header("📊 Resume Analytics Dashboard")

    # ==========================
    # KPI Cards
    # ==========================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        kpi_card(
            "ATS Score",
            f"{ats_score}/100",
            "⭐"
        )

    with col2:
        kpi_card(
            "Career Score",
            f"{career['score']}/100",
            "🚀"
        )

    with col3:
        kpi_card(
            "Detected Skills",
            len(detected_skills),
            "🧠"
        )

    with col4:
        kpi_card(
            "Missing Skills",
            len(missing_skills),
            "❌"
        )

    st.markdown("---")

    # ==========================
    # Career Summary
    # ==========================

    st.subheader("🎯 Career Summary")

    st.success(
        f"Recommended Role: **{best_role['Role']}**"
    )

    st.info(
        f"Career Readiness: **{career['level']}**"
    )

    st.info(
        f"Role Match Score: **{best_role['Score']}%**"
    )

    st.markdown("---")

    # ==========================
    # Resume Strengths
    # ==========================

    st.subheader("💪 Resume Strengths")

    if review["strengths"]:

        for strength in review["strengths"]:
            st.success(strength)

    else:

        st.info("No strengths detected.")

    st.markdown("---")

    # ==========================
    # Suggestions
    # ==========================

    st.subheader("💡 Resume Suggestions")

    if review["suggestions"]:

        for suggestion in review["suggestions"]:
            st.warning(suggestion)

    else:

        st.success("Excellent Resume!")
    
    st.markdown("---")
    st.subheader("📈 Resume Analytics")

    col1, col2 = st.columns(2)

    with col1:
        skills_chart(detected_skills)

    with col2:
        missing_skills_chart(missing_skills)