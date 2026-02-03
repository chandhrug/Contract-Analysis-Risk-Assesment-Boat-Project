
STANDARD_CLAUSES = {
    "indemnity": "Each party shall indemnify the other only for direct losses caused by its own negligence.",
    "termination": "Either party may terminate with 30 days written notice."
}

def suggest_alternative(clause):
    clause = clause.lower()
    if "indemnify" in clause:
        return STANDARD_CLAUSES["indemnity"]
    if "terminate" in clause:
        return STANDARD_CLAUSES["termination"]
    return "No alternative needed"
