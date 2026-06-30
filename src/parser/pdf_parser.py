import pdfplumber


def extract_text_from_pdf(uploaded_file):

    extracted_text = ""

    try:
        uploaded_file.seek(0)

        with pdfplumber.open(uploaded_file) as pdf:

             for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:
                        extracted_text += page_text + "\n"

        return extracted_text.strip()

    except Exception as e:
        return f"ERROR: {e}"