import streamlit as st
from src.parser.file_validator import validate_pdf
from src.parser.pdf_parser import extract_text_from_pdf
from src.utils.text_cleaner import clean_resume_text
from src.utils.resume_stats import get_resume_statistics
from src.extractor.skill_extractor import (
    load_skills,
    extract_skills
)

skills = load_skills()

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="SkillPilot AI 2.0",
    page_icon="🚀",
    layout="wide"
)

st.markdown("---")

st.header("📄 Resume Upload")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    is_valid, message = validate_pdf(uploaded_file)

    if is_valid:

        st.success(message)

        st.write("### File Information")

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**Filename:** {uploaded_file.name}")

        with col2:
            st.write(f"**Size:** {round(uploaded_file.size / 1024, 2)} KB")

        st.markdown("---")

        # ===========================
        # Extract Resume Text
        # ===========================
        resume_text = extract_text_from_pdf(uploaded_file)

        if resume_text.startswith("ERROR"):

            st.error(resume_text)

        elif resume_text.strip() == "":

            st.warning("No text could be extracted from this PDF.")

        else:

            # ===========================
            # Clean Resume Text
            # ===========================
            cleaned_text = clean_resume_text(resume_text)

            # ===========================
            # Resume Statistics
            # ===========================
            stats = get_resume_statistics(cleaned_text)

            st.subheader("📊 Resume Statistics")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("📝 Words", stats["Words"])

            with col2:
                st.metric("🔤 Characters", stats["Characters"])

            with col3:
                st.metric("📄 Lines", stats["Lines"])

            with col4:
                st.metric("⏱ Reading Time", stats["Reading Time"])

            st.markdown("---")

            # ===========================
            # Skill Extraction
            # ===========================
            detected_skills = extract_skills(cleaned_text, skills)

            st.subheader("🧠 Detected Skills")

            if detected_skills:
                for skill in detected_skills:
                    st.success(skill)
            else:
                st.warning("No skills detected.")

            st.markdown("---")

            # ===========================
            # Resume Preview
            # ===========================
            st.subheader("📄 Resume Preview")

            with st.expander("View Resume Text", expanded=True):
                st.text_area(
                    "Extracted Resume",
                    cleaned_text,
                    height=400
                )

    else:
        st.error(message)

# -------------------------------
# Header
# -------------------------------
st.title("🚀 SkillPilot AI 2.0")
st.subheader("AI Skill Gap Mapper & Placement Roadmap Generator")

st.markdown("---")

# -------------------------------
# Welcome Section
# -------------------------------
st.header("👋 Welcome")

st.write("""
SkillPilot AI is an AI-powered platform that helps students analyze their resumes,
compare them with industry job requirements, identify missing skills,
and generate personalized learning roadmaps.

Our goal is to improve placement readiness and help students make smarter career decisions.
""")

st.markdown("---")

# -------------------------------
# Problem Statement
# -------------------------------
st.header("📌 Problem Statement")

st.write("""
Many students apply for jobs without knowing whether their skills match industry expectations.
They often receive rejections without understanding what they need to improve.

SkillPilot AI bridges this gap by providing an intelligent resume analysis system.
""")

st.markdown("---")

# -------------------------------
# Features (Coming Soon)
# -------------------------------
st.header("🚀 Upcoming Features")

st.markdown("""
- 📄 Resume Upload
- 📑 Resume Parsing
- 🧠 Skill Extraction
- 🤖 AI-Based Role Matching
- 📊 Skill Gap Analysis
- 🛣 Personalized Learning Roadmap
- 📈 Interactive Dashboard
""")

st.markdown("---")

# -------------------------------
# Technology Stack
# -------------------------------
st.header("🛠 Technology Stack")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
### Backend
- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
    """)

with col2:
    st.markdown("""
### AI & NLP
- spaCy
- Sentence Transformers
- RapidFuzz
- Plotly
    """)

st.markdown("---")

# -------------------------------
# Project Status
# -------------------------------
st.header("📌 Project Status")

st.info("🚧 Version 1.0 (MVP) is currently under development.")

st.success("Day 1 Progress: Project Setup Completed")

st.markdown("---")

# -------------------------------
# Footer
# -------------------------------
st.caption("© 2026 SkillPilot AI | Built with ❤️ using Python & Streamlit")
