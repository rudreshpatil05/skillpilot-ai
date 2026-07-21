from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from datetime import datetime


def generate_report(
    filename,
    best_role,
    detected_skills,
    missing_skills,
    ats_score,
    career,
    ai_suggestions
):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b><font size=18>SkillPilot AI Career Report</font></b>", styles["Title"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(f"<b>Generated:</b> {datetime.now().strftime('%d-%m-%Y %H:%M')}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(f"<b>Best Role:</b> {best_role}", styles["Heading2"]))

    story.append(Paragraph(f"<b>ATS Score:</b> {ats_score}%", styles["Heading2"]))

    story.append(Paragraph(f"<b>Career Readiness:</b> {career}", styles["Heading2"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Detected Skills</b>", styles["Heading2"]))

    for skill in detected_skills:
        story.append(Paragraph(f"• {skill}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Missing Skills</b>", styles["Heading2"]))

    for skill in missing_skills:
        story.append(Paragraph(f"• {skill}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>AI Resume Suggestions</b>", styles["Heading2"]))

    story.append(Paragraph(ai_suggestions.replace("\n", "<br/>"), styles["Normal"]))

    doc.build(story)