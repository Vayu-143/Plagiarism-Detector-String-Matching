from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_pdf(report):

    pdf = SimpleDocTemplate(

        "reports/plagiarism_report.pdf"

    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(

        Paragraph(

            "Plagiarism Detection Report",

            styles["Title"]

        )

    )

    elements.append(

        Spacer(1, 12)

    )

    for key, value in report.items():

        elements.append(

            Paragraph(

                f"<b>{key}</b>: {value}",

                styles["BodyText"]

            )

        )

    pdf.build(elements)