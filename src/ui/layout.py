import streamlit as st


def setup_sidebar():

    st.sidebar.title("🚀 SkillPilot AI")

    st.sidebar.markdown("---")

    st.sidebar.success("Navigation")

    st.sidebar.write("📄 Resume Upload")

    st.sidebar.write("📊 Resume Analysis")

    st.sidebar.write("🎯 Career Match")

    st.sidebar.write("⭐ ATS Review")

    st.sidebar.write("🛣 Learning Roadmap")

    st.sidebar.write("🤖 AI Chatbot")

    st.sidebar.write("📈 Dashboard")

    st.sidebar.markdown("---")

    st.sidebar.info(
        "Version 1.0\n\nBuilt using Python + Streamlit"
    )