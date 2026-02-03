import streamlit as st
from nlp_engine import *
from risk_engine import *
from templates import *
from llm_engine import *
from audit import *
from utils import *
from language_normalizer import normalize_hindi_to_english
import pdfplumber
from docx import Document

st.set_page_config(page_title="GenAI Legal Assistant", layout="wide")
st.title("📄 GenAI Legal Assistant for Indian SMEs")

# ------------------------------
# FILE UPLOADER OR TEXT AREA
# ------------------------------
uploaded_file = st.file_uploader("Upload Contract (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

if uploaded_file:
    # Read file
    if uploaded_file.name.endswith(".pdf"):
        text = ""
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    elif uploaded_file.name.endswith(".docx"):
        doc = Document(uploaded_file)
        text = "\n".join([p.text for p in doc.paragraphs])
    else:  # TXT
        text = uploaded_file.read().decode("utf-8")

    st.text_area("Contract Text Extracted", text, height=200)
else:
    # Fallback to textarea
    text = st.text_area("Or Paste Contract Text Here")

# ------------------------------
# ANALYZE BUTTON
# ------------------------------
if st.button("Analyze"):
    if not text.strip():
        st.warning("Please provide contract text by uploading a file or pasting it.")
        st.stop()

    normalized_text = normalize_hindi_to_english(text)

    # NLP tasks
    contract_type = classify_contract(normalized_text)
    clauses = extract_clauses(normalized_text)
    entities = extract_entities(normalized_text)

    # Risk analysis
    risks = []
    for clause in clauses:
        role = classify_clause_role(clause)
        risk = assess_clause_risk(clause)
        risks.append(risk)

    score = contract_risk_score(risks)
    summary = generate_summary(contract_type, score)

    # Save in session_state
    st.session_state.contract_type = contract_type
    st.session_state.clauses = clauses
    st.session_state.risks = risks
    st.session_state.score = score
    st.session_state.summary = summary

    # Display results
    st.subheader(f"Contract Type: {contract_type}")
    st.metric("Overall Risk Score", f"{score}%")
    st.subheader("Summary")
    st.write(summary)

    for i, clause in enumerate(clauses, 1):
        role = classify_clause_role(clause)
        risk = assess_clause_risk(clause)
        with st.expander(f"Clause {i} | {risk} | {role}"):
            st.write("**Clause Text**")
            st.write(clause)
            st.write("**Explanation (Simple English)**")
            st.write(explain_clause_simple(clause))
            st.write("**Suggested Alternative**")
            st.write(suggest_alternative(clause))

    # Audit log
    log_action("ANALYSIS_COMPLETE", {"risk_score": score})

# ------------------------------
# EXPORT PDF BUTTON
# ------------------------------
if st.button("Export PDF"):
    if "contract_type" not in st.session_state:
        st.warning("Please click Analyze first!")
        st.stop()

    contract_type = st.session_state.contract_type
    clauses = st.session_state.clauses
    risks = st.session_state.risks
    score = st.session_state.score
    summary = st.session_state.summary

    # Prepare full text for PDF
    full_text = f"Contract Type: {contract_type}\nOverall Risk Score: {score}%\n\nSummary:\n{summary}\n\nClauses:\n"
    for i, clause in enumerate(clauses, 1):
        role = classify_clause_role(clause)
        risk = assess_clause_risk(clause)
        explanation = explain_clause_simple(clause)
        alt = suggest_alternative(clause)
        full_text += f"Clause {i} | {risk} | {role}\n{clause}\nExplanation: {explanation}\nSuggested Alternative: {alt}\n\n"

    # Generate PDF
    file_path = export_pdf(full_text)

    # Streamlit download button
    with open(file_path, "rb") as f:
        st.download_button(
            label="Download PDF",
            data=f,
            file_name="contract_analysis.pdf",
            mime="application/pdf"
        )
