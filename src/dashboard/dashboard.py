import streamlit as st


def show_dashboard(
    detected_skills,
    missing_skills,
    ats_score,
    career
):
    """
    Displays Resume Dashboard
    """

    st.markdown("---")
    st.header("📊 Resume Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "✅ Detected Skills",
            len(detected_skills)
        )

        st.metric(
            "⭐ ATS Score",
            ats_score
        )

    with col2:
        st.metric(
            "❌ Missing Skills",
            len(missing_skills)
        )

        st.metric(
            "🚀 Career Score",
            career["score"]
        )

    st.markdown("---")

    st.subheader("Progress")

    st.write("ATS Score")
    st.progress(ats_score / 100)

    st.write("Career Readiness")
    st.progress(career["score"] / 100)

    st.markdown("---")

    st.subheader("Quick Summary")

    st.success("Resume Uploaded")

    st.success("Resume Parsed")

    st.success("Skills Extracted")

    st.success("Role Matched")

    st.success("Roadmap Generated")