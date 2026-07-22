from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import inch


def generate_pdf_report(
    filename,
    best_role,
    detected_skills,
    missing_skills,
    ats_score,
    career,
    roadmap,
    review,
):
    """
    Generate SkillPilot AI Resume Analysis Report

    Parameters
    ----------
    filename : str
        Output PDF filename.

    best_role : dict
        Example:
        {
            "Role": "Machine Learning Engineer",
            "Score": 91
        }

    detected_skills : list

    missing_skills : list

    ats_score : int

    career : dict
        Example:
        {
            "level": "Intermediate",
            "score": 82
        }

    roadmap : list

    review : dict
    """

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER
    title_style.textColor = HexColor("#1F4E79")

    heading = styles["Heading2"]
    heading.textColor = HexColor("#1F4E79")

    normal = styles["BodyText"]

    story = []

    # ==================================================
    # Title
    # ==================================================

    story.append(Paragraph("SkillPilot AI Resume Analysis Report", title_style))
    story.append(Spacer(1, 0.25 * inch))

    # ==================================================
    # Career Summary
    # ==================================================

    story.append(Paragraph("Career Summary", heading))

    role = best_role.get("Role", "Not Available")
    score = best_role.get("Score", 0)

    story.append(Paragraph(f"<b>Recommended Role:</b> {role}", normal))
    story.append(Paragraph(f"<b>Role Match:</b> {score}%", normal))
    story.append(Paragraph(f"<b>ATS Score:</b> {ats_score}/100", normal))

    career_level = career.get("level", "Unknown")
    career_score = career.get("score", 0)

    story.append(
        Paragraph(
            f"<b>Career Readiness:</b> {career_level} ({career_score}/100)",
            normal,
        )
    )

    story.append(Spacer(1, 0.25 * inch))

    # ==================================================
    # Detected Skills
    # ==================================================

    story.append(Paragraph("Detected Skills", heading))

    if detected_skills:

        for skill in detected_skills:
            story.append(Paragraph(f"• {skill}", normal))

    else:
        story.append(Paragraph("No skills detected.", normal))

    story.append(Spacer(1, 0.25 * inch))

    # ==================================================
    # Missing Skills
    # ==================================================

    story.append(Paragraph("Missing Skills", heading))

    if missing_skills:

        for skill in missing_skills:
            story.append(Paragraph(f"• {skill}", normal))

    else:
        story.append(
            Paragraph("Excellent! No major missing skills found.", normal)
        )

    story.append(Spacer(1, 0.25 * inch))

    # ==================================================
    # Learning Roadmap
    # ==================================================

    story.append(Paragraph("Personalized Learning Roadmap", heading))

    if roadmap:

        for item in roadmap:

            week = item.get("Week", "-")
            skill = item.get("Skill", "-")
            difficulty = item.get("Difficulty", "-")
            days = item.get("Days", "-")
            project = item.get("Project", "-")

            story.append(
                Paragraph(
                    f"<b>Week {week}</b>",
                    normal,
                )
            )

            story.append(
                Paragraph(f"Skill : {skill}", normal)
            )

            story.append(
                Paragraph(f"Difficulty : {difficulty}", normal)
            )

            story.append(
                Paragraph(f"Estimated Days : {days}", normal)
            )

            story.append(
                Paragraph(f"Mini Project : {project}", normal)
            )

            resources = item.get("Resources", [])

            if resources:

                story.append(
                    Paragraph("<b>Resources</b>", normal)
                )

                for resource in resources:
                    story.append(
                        Paragraph(f"• {resource}", normal)
                    )

            story.append(Spacer(1, 0.15 * inch))

    else:

        story.append(
            Paragraph("Roadmap unavailable.", normal)
        )

    story.append(Spacer(1, 0.25 * inch))

    # ==================================================
    # Resume Strengths
    # ==================================================

    story.append(Paragraph("Resume Strengths", heading))

    strengths = review.get("strengths", [])

    if strengths:

        for strength in strengths:
            story.append(
                Paragraph(f"• {strength}", normal)
            )

    else:
        story.append(
            Paragraph("No strengths detected.", normal)
        )

    story.append(Spacer(1, 0.25 * inch))

    # ==================================================
    # Resume Suggestions
    # ==================================================

    story.append(Paragraph("Resume Improvement Suggestions", heading))

    suggestions = review.get("suggestions", [])

    if suggestions:

        for suggestion in suggestions:
            story.append(
                Paragraph(f"• {suggestion}", normal)
            )

    else:
        story.append(
            Paragraph("Great Resume! No major improvements required.", normal)
        )

    story.append(Spacer(1, 0.30 * inch))

    # ==================================================
    # Footer
    # ==================================================

    story.append(
        Paragraph(
            "<b>Generated by SkillPilot AI</b>",
            styles["Heading3"],
        )
    )

    story.append(
        Paragraph(
            "AI Resume Screening • Skill Gap Analysis • Career Roadmap • ATS Evaluation",
            normal,
        )
    )

    doc.build(story)