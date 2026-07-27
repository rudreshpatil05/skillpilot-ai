import streamlit as st
from src.parser.file_validator import validate_pdf
from src.parser.pdf_parser import extract_text_from_pdf
from src.reviewer import review_resume
from src.semantic.explanation import generate_match_explanation
from src.utils.text_cleaner import clean_resume_text
from src.utils.resume_stats import get_resume_statistics
from src.extractor.skill_extractor import (
    load_skills,
    extract_skills
)
from src.matching.role_matcher import load_roles, match_roles
from src.analyzer.future_score import calculate_future_score
from src.analyzer.gap_analyzer import analyze_skill_gap
#from src.reports import generate_pdf_report
from src.visualization.charts import role_match_chart
from src.roadmap.roadmap_generator import generate_learning_roadmap
from src.reviewer import review_resume
from src.chatbot import answer_resume_question
from src.ui import setup_sidebar
from src.dashboard.dashboard import show_dashboard
from src.semantic.semantic_matcher import semantic_role_match
from src.visualization.semantic_chart import semantic_chart
from src.dashboard.kpi_cards import kpi_card
from src.recommendation import recommend_learning
from src.reviewer import review_resume
from src.interview.interview_generator import generate_interview_questions
from src.chatbot.chatbot import ask_chatbot
from src.chatbot.prompts import SUGGESTED_QUESTIONS
from src.chatbot.chatbot import ask_chatbot
import src.reports.pdf_report as pdf_report
import inspect

import streamlit as st

st.title("MAIN APP")

st.success("App started")

st.write("Step 1")

import time

time.sleep(1)

st.write("Step 2")

st.write("Everything works")

skills = load_skills()
roles = load_roles()

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="SkillPilot AI 2.0",
    page_icon="🚀",
    layout="wide"
)

setup_sidebar()

st.title("🚀 SkillPilot AI 2.0")
st.subheader("AI Skill Gap Mapper & Placement Roadmap Generator")

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

            review = review_resume(
                detected_skills,
                resume_text
            )

            st.subheader("🧠 Detected Skills")

            if detected_skills:

                cols = st.columns(3)

                for i, skill in enumerate(detected_skills):

                    with cols[i % 3]:
                        st.success(skill)

            else:

                st.warning("No skills detected.")

            st.markdown("---")

            # ===========================
            # Resume Preview
            # ===========================

            st.subheader("📄 Resume Preview")

            preview = cleaned_text[:8000]

            with st.expander("View Resume Text", expanded=True):

                st.text_area(
                    "Extracted Resume",
                    preview,
                    height=400
                )

            # ===========================
            # Role Matching
            # ===========================

            results = match_roles(
                detected_skills,
                roles
            )

            skills_text = " ".join(detected_skills)

            semantic_result = semantic_role_match(skills_text)

            if len(results) > 0:

                best_role = results[0]

                if semantic_result:

                    best_role = {
                        **best_role,
                        "Role": semantic_result.get("Role", best_role["Role"]),
                        "Score": semantic_result.get("Score", best_role["Score"])
                    }

                interview_questions = generate_interview_questions(
                    best_role["Role"]
                )

                career = calculate_future_score(best_role)

                explanation = generate_match_explanation(
                    best_role,
                    detected_skills
                )

                st.subheader("🎯 Best Career Match")

                st.success(best_role["Role"])

                match_score = min(max(best_role["Score"], 0), 100)

                st.progress(match_score / 100)

                kpi_card(
                    "Match Score",
                    f"{match_score}%",
                    "🎯"
                )

                st.subheader("⭐ Career Readiness")

                career_score = min(max(career["score"], 0), 100)

                st.progress(career_score / 100)

                kpi_card(
                    "Career Score",
                    f"{career_score}/100",
                    "⭐"
                )

                st.success(career["level"])

                st.markdown("---")

                st.subheader("🧠 Why this role?")

                st.info(explanation.get("confidence", ""))

                st.write("### ✅ Your Strengths")

                for skill in explanation.get("strengths", []):

                    st.success(skill)

                st.write("### ❌ Missing Skills")

                for skill in explanation.get("missing", []):

                    st.error(skill)

                st.write("### 🚀 Recommendation")

                st.warning(
                    explanation.get(
                        "recommendation",
                        "No recommendation available."
                    )
                )

                st.markdown("---")

                st.subheader("🏆 Top Matching Roles")

                fig = semantic_chart(results)

                if fig is not None:

                    st.plotly_chart(
                        fig,
                        use_container_width=True,
                        key="role_match_chart"
                    )

            else:

                st.warning("No matching role found.")
        # ===========================
        # Skill Gap Analysis
        # ===========================

        # Analyze missing skills
        missing_skills = analyze_skill_gap(
            detected_skills,
            best_role
        )

        # ATS Score
        ats_score = review["score"]

        # ===========================
        # Resume Dashboard
        # ===========================

        try:
            show_dashboard(
                detected_skills=detected_skills,
                missing_skills=missing_skills,
                ats_score=ats_score,
                career=career,
                best_role=best_role,
                review=review
            )

        except Exception as e:
            st.error("Dashboard Error")
            st.exception(e)

        # ==========================
        # Skills Overview Chart
        # ==========================

        st.subheader("📈 Skills Overview")

        skills_chart_data = {
            "Category": [
                "Detected Skills",
                "Missing Skills"
            ],
            "Count": [
                len(detected_skills),
                len(missing_skills)
            ]
        }

        st.bar_chart(
            skills_chart_data,
            x="Category",
            y="Count"
        )

        # ==========================
        # Learning Recommendation
        # ==========================

        learning = recommend_learning(best_role["Missing"])

        st.subheader("📚 Recommended Learning")

        for item in learning:
            st.info(
                f"**{item['Skill']}** → {item['Recommendation']}"
            )
        # ==========================
        # Resume Analytics
        # ==========================

        st.markdown("---")
        st.subheader("📊 Resume Analytics")

        import pandas as pd

        analytics = pd.DataFrame({
            "Category": [
                "Detected Skills",
                "Missing Skills"
            ],
            "Count": [
                len(detected_skills),
                len(missing_skills)
            ]
        })

        st.caption("Overall Resume Skill Distribution")

        st.dataframe(
            analytics,
            use_container_width=True,
            hide_index=True
        )

        st.bar_chart(
            analytics,
            x="Category",
            y="Count"
        )

        # ===========================
        # Personalized Learning Roadmap
        # ===========================

        roadmap = generate_learning_roadmap(missing_skills)

        st.markdown("---")
        st.subheader("🛣 Personalized Learning Roadmap")

        for step in roadmap:

            st.info(f"📅 Week {step['Week']}")

            st.write(f"**Skill:** {step['Skill']}")

            st.write(f"**Difficulty:** {step['Difficulty']}")

            st.write(f"**Estimated Days:** {step['Days']}")

            st.write(f"**Mini Project:** {step['Project']}")

            st.write("### 📚 Resources")

            for resource in step["Resources"]:
                st.write(f"• {resource}")

            st.markdown("---")

            # ===========================
        # AI Interview Preparation
        # ===========================

        st.markdown("---")
        st.subheader("🎤 AI Interview Preparation")

        if "interview_questions" in locals():

            st.markdown("### 🟢 Easy Questions")
            for question in interview_questions.get("Easy", []):
                st.info(question)

            st.markdown("### 🟡 Medium Questions")
            for question in interview_questions.get("Medium", []):
                st.warning(question)

            st.markdown("### 🔴 Hard Questions")
            for question in interview_questions.get("Hard", []):
                st.error(question)

        else:
            st.warning("Interview questions are not available.")


        # ===========================
        # ATS Resume Review
        # ===========================

        ats_score = review["score"]

        st.markdown("---")
        st.subheader("⭐ ATS Resume Review")

        st.metric("ATS Score", f"{ats_score}/100")
        st.progress(ats_score / 100)

        if ats_score >= 85:
            st.success("Excellent ATS Score 🚀")
        elif ats_score >= 70:
            st.info("Good ATS Score 👍")
        elif ats_score >= 50:
            st.warning("Average ATS Score ⚠️")
        else:
            st.error("Low ATS Score ❌")


        # ===========================
        # Resume Strengths
        # ===========================

        st.subheader("💪 Resume Strengths")

        for strength in review.get("strengths", []):
            st.success(strength)


        # ===========================
        # Resume Suggestions
        # ===========================

        st.subheader("💡 Resume Suggestions")

        for suggestion in review.get("suggestions", []):
            st.warning(suggestion)


        # ===========================
        # PDF Report
        # ===========================

        st.markdown("---")
        st.subheader("📄 Download Resume Report")

        try:

            pdf_filename = "SkillPilot_AI_Report.pdf"

            pdf_report.generate_pdf_report(
                filename=pdf_filename,
                best_role=best_role,
                detected_skills=detected_skills,
                missing_skills=missing_skills,
                ats_score=ats_score,
                career=career,
                roadmap=roadmap,
                review=review
            )

            with open(pdf_filename, "rb") as pdf_file:

                st.download_button(
                    label="📥 Download SkillPilot AI Report",
                    data=pdf_file,
                    file_name=pdf_filename,
                    mime="application/pdf",
                    key="download_pdf_report"
                )

        except Exception as e:
            st.exception(e)


        # ===========================
        # SkillPilot AI Career Assistant
        # ===========================

        st.markdown("---")
        st.subheader("🤖 SkillPilot AI Career Assistant")

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        st.subheader("💡 Suggested Questions")

        cols = st.columns(2)

        for i, prompt in enumerate(SUGGESTED_QUESTIONS):

            with cols[i % 2]:

                if st.button(prompt, key=f"prompt_{i}"):
                    st.session_state.selected_question = prompt

        default_question = st.session_state.get(
            "selected_question",
            ""
        )

        user_question = st.text_input(
            "Ask anything about Resume, AI, Data Science or Career",
            value=default_question,
            key="career_chat_input"
        )

        if st.button("🚀 Ask AI"):

            if user_question:

                with st.spinner("🤖 Thinking..."):

                    answer = ask_chatbot(
                        question=user_question,
                        best_role=best_role,
                        detected_skills=detected_skills,
                        missing_skills=missing_skills,
                        ats_score=ats_score,
                        career=career
                    )

                st.session_state.chat_history.append({
                    "user": user_question,
                    "assistant": answer
                })

                st.success(answer)

            else:
                st.warning("Please enter a question.")
            # ==========================
            # Chat History
            # ==========================

            for chat in st.session_state.chat_history:

                with st.chat_message("user"):
                    st.write(chat["user"])

                with st.chat_message("assistant"):
                    st.write(chat["assistant"])


            # ==========================================================
            # AI Resume Improvement Suggestions
            # ==========================================================

            st.markdown("---")
            st.subheader("💡 AI Resume Improvement Suggestions")

            if "ai_suggestions" not in st.session_state:
                st.session_state["ai_suggestions"] = ""


            if st.button("✨ Generate AI Suggestions"):

                with st.spinner("Analyzing your resume..."):

                    suggestion_prompt = f"""
            You are an expert Resume Reviewer.

            Analyze this resume.

            Best Role:
            {best_role}

            Detected Skills:
            {detected_skills}

            Missing Skills:
            {missing_skills}

            ATS Score:
            {ats_score}

            Career Readiness:
            {career}

            Provide professional resume improvement suggestions.

            Include:

            1. Resume Improvements
            2. ATS Improvements
            3. Skills to Learn
            4. Projects to Build
            5. Certifications
            6. Interview Preparation Tips

            Use bullet points.
            """

                    st.session_state["ai_suggestions"] = ask_chatbot(
                        question=suggestion_prompt,
                        best_role=best_role,
                        detected_skills=detected_skills,
                        missing_skills=missing_skills,
                        ats_score=ats_score,
                        career=career
                    )

                st.success("AI Suggestions Generated Successfully!")


            # Always display suggestions after generation

            if st.session_state["ai_suggestions"]:

                st.subheader("📝 AI Suggestions")

                st.write(st.session_state["ai_suggestions"])

                st.markdown("---")
                st.subheader("📄 Download AI Career Report")

                pdf_filename = "SkillPilot_AI_Report.pdf"

                if st.button("📄 Generate PDF Report"):

                    pdf_report.generate_pdf_report(
                        filename=pdf_filename,
                        best_role=best_role,
                        detected_skills=detected_skills,
                        missing_skills=missing_skills,
                        ats_score=ats_score,
                        career=career,
                        roadmap=roadmap,
                        review=review
                    )

                if pdf_filename:

                    try:
                        with open(pdf_filename, "rb") as pdf_file:

                            st.download_button(
                                label="⬇ Download Report",
                                data=pdf_file,
                                file_name=pdf_filename,
                                mime="application/pdf",
                                key="download_ai_report"
                            )

                    except FileNotFoundError:
                        st.warning("Generate the PDF first.")


# -------------------------------
# Header
# -------------------------------
st.title("🚀 SkillPilot AI 2.0")
st.subheader("AI Skill Gap Mapper & Placement Roadmap Generator")

st.markdown("---")

st.markdown("---")

with st.expander("ℹ About SkillPilot AI", expanded=False):

    st.header("👋 Welcome")

    st.write("""
    SkillPilot AI is an AI-powered Resume Analyzer that helps students
    identify missing skills, improve ATS score, discover suitable job
    roles, and generate personalized learning roadmaps.
    """)

    st.markdown("---")

    st.subheader("🚀 Features")

    st.markdown("""
    ✅ Resume Upload

    ✅ Resume Parsing

    ✅ Skill Extraction

    ✅ AI Role Matching

    ✅ ATS Resume Review

    ✅ Career Readiness Score

    ✅ Personalized Learning Roadmap

    ✅ Resume Dashboard

    ✅ AI Resume Chatbot
    """)

    st.markdown("---")

    st.subheader("🛠 Technology Stack")

    st.markdown("""
    • Python

    • Streamlit

    • Pandas

    • Scikit-learn

    • Plotly

    • FastAPI (Upcoming)

    • Machine Learning
    """)

    st.markdown("---")

    st.info("Version 1.0 MVP")