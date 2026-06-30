def validate_pdf(uploaded_file):
    
    if uploaded_file is None:
        return False, "No file uploaded."

    if uploaded_file.type != "application/pdf":
        return False, "Only PDF files are allowed."

    if uploaded_file.size == 0:
        return False, "Uploaded file is empty."

    max_size = 5 * 1024 * 1024  # 5 MB

    if uploaded_file.size > max_size:
        return False, "File size exceeds 5 MB."

    return True, "Validation Successful"