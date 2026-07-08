import streamlit as st


def show_summary(
    best_role,
    detected_skills,
    missing_skills,
    ats_score,
    career
):

    st.markdown("---")

    st.header("📌 Resume Analysis Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🎯 Best Role",
            best_role["Role"]
        )

    with col2:
        st.metric(
            "⭐ ATS Score",
            f"{ats_score}/100"
        )

    with col3:
        st.metric(
            "🚀 Career Score",
            f"{career['score']}/100"
        )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.success(
            f"Detected Skills : {len(detected_skills)}"
        )

    with col2:

        st.error(
            f"Missing Skills : {len(missing_skills)}"
        )