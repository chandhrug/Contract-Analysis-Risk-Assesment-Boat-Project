# 📄 GenAI Legal Assistant for Indian SMEs

A Streamlit-based GenAI-powered legal assistant that helps **Indian SMEs** understand contracts, identify legal risks, and receive **plain-English explanations**.  
Supports **English and Hindi contracts** (Hindi is fully translated to English before analysis).

---

## 🚀 Features

- Upload contracts: **PDF / DOCX / TXT**
- **Full sentence Hindi → English translation**
- Contract type classification
- Clause-by-clause analysis
- Risk detection (Low / Medium / High)
- Plain-English explanations & suggested alternatives
- Overall contract risk score
- **PDF export** for legal consultation
- Local **audit logging** (no external storage)

---

## 🧱 Project Structure

project/
│── app.py # Main Streamlit app
│── nlp_engine.py # NLP tasks (classification, clauses, roles)
│── risk_engine.py # Risk scoring logic
│── llm_engine.py # Plain-language explanations (mock GenAI)
│── templates.py # Standard SME templates
│── audit.py # Audit trail logging
│── utils.py # PDF export utility
│── language_normalizer.py # Hindi → English translation
│── README.md
