import re

def classify_contract(text):
    text = text.lower()
    if "employment" in text:
        return "Employment Agreement"
    if "vendor" in text or "service" in text:
        return "Vendor / Service Contract"
    if "lease" in text or "rent" in text:
        return "Lease Agreement"
    return "General Contract"

def extract_clauses(text):
    clauses = []
    for line in text.split("\n"):
        line = line.strip()
        if len(line) > 20:
            clauses.append(line)
    return clauses

def extract_entities(text):
    entities = {
        "Amounts": re.findall(r"\bINR\s?\d+[,\d]*", text),
        "Dates": re.findall(r"\b\d{1,2}\s\w+\s\d{4}", text),
    }
    return entities

def classify_clause_role(clause):
    c = clause.lower()
    if "shall" in c or "must" in c:
        return "Obligation"
    if "may" in c:
        return "Right"
    if "shall not" in c or "prohibited" in c:
        return "Prohibition"
    return "Neutral"
