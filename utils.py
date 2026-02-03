import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# ------------------------------
# PDF Export Function
# ------------------------------
def export_pdf(text, filename="contract_analysis.pdf"):
    """
    Generate PDF from given text and return the file path.
    """
    file_path = os.path.join(os.getcwd(), filename)
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    lines = text.split("\n")
    y = height - 50  # Start from top

    for line in lines:
        if y < 50:  # New page if near bottom
            c.showPage()
            y = height - 50
        c.drawString(50, y, line)
        y -= 15

    c.save()
    return file_path

# ------------------------------
# Additional Utility Functions
# ------------------------------

def clean_text(text):
    """
    Simple text cleaning: remove extra spaces, tabs, and line breaks.
    """
    return " ".join(text.split())

def save_json(data, filename="audit_log.json"):
    """
    Save dictionary data to JSON file.
    """
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return filename

def load_json(filename="audit_log.json"):
    """
    Load JSON file into a dictionary.
    """
    import json
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}
