try:
    from .pdf_report import generate_pdf_report
except ModuleNotFoundError:

    def generate_pdf_report(*args, **kwargs):
        raise ModuleNotFoundError(
            "ReportLab is not installed."
        )