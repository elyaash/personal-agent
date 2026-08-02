import docx2txt
import os

def get_resume_content():
    resume_path = os.path.join("docs", "Prakashsinh_Rajput_NodeJS.docx")
    if not os.path.exists(resume_path):
        return "Resume file not found."
    try:
        text = docx2txt.process(resume_path)
        return text
    except Exception as e:
        return f"Error reading resume: {str(e)}"
