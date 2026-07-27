import streamlit as st
from .charts import skills_chart, missing_skills_chart
from .kpi_cards import kpi_card
import inspect

print("=" * 80)
print("KPI FUNCTION :", kpi_card)
print("KPI FILE     :", inspect.getfile(kpi_card))
print("KPI SOURCE")
print(inspect.getsource(kpi_card))
print("=" * 80)
#st.write(inspect.getfile(kpi_card))

def show_dashboard(
    detected_skills,
    missing_skills,
    ats_score,
    career,
    best_role,
    review
):
    """
    Displays the Resume Analytics Dashboard.
    """

    st.markdown("---")
    st.header("📊 Resume Analytics Dashboard")

    # =====================================
    # KPI CARDS
    # =====================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        kpi_card(
            title="ATS Score",
            value=f"{ats_score}/100",
            icon="⭐"
        )

    with col2:
        kpi_card(
            title="Career Score",
            value=f"{career.get('score', 0)}/100",
            icon="🚀"
        )

    with col3:
        kpi_card(
            title="Detected Skills",
            value=str(len(detected_skills)),
            icon="🧠"
        )

    with col4:
        kpi_card(
            title="Missing Skills",
            value=str(len(missing_skills)),
            icon="❌"
        )

    st.markdown("---")

    # =====================================
    # Career Summary
    # =====================================

    st.subheader("🎯 Career Summary")

    st.success(
        f"Recommended Role: **{best_role.get('Role','N/A')}**"
    )

    st.info(
        f"Career Readiness: **{career.get('level','N/A')}**"
    )

    st.info(
        f"Role Match Score: **{best_role.get('Score',0)}%**"
    )

    st.markdown("---")

    # =====================================
    # Resume Strengths
    # =====================================

    st.subheader("💪 Resume Strengths")

    strengths = review.get("strengths", [])

    if strengths:
        for strength in strengths:
            st.success(strength)
    else:
        st.info("No strengths detected.")

    st.markdown("---")

    # =====================================
    # Resume Suggestions
    # =====================================

    st.subheader("💡 Resume Suggestions")

    suggestions = review.get("suggestions", [])

    if suggestions:
        for suggestion in suggestions:
            st.warning(suggestion)
    else:
        st.success("Excellent Resume!")

    st.markdown("---")

    # =====================================
    # Charts
    # =====================================

    st.subheader("📈 Resume Analytics")

    col1, col2 = st.columns(2)

    with col1:
        try:
            skills_chart(detected_skills)
        except Exception as e:
            st.error(f"Skills Chart Error: {e}")

    with col2:
        try:
            missing_skills_chart(missing_skills)
        except Exception as e:
            st.error(f"Missing Skills Chart Error: {e}")