




def assess_clause_risk(clause):
    clause_lower = clause.lower()
    if "penalty" in clause_lower or "fine" in clause_lower:
        return "High Risk"
    if "terminate at any time" in clause_lower or "unilateral termination" in clause_lower:
        return "High Risk"
    if "non compete" in clause_lower or "non-compete" in clause_lower:
        return "Medium Risk"
    if "indemnify" in clause_lower:
        return "Medium Risk"
    return "Low Risk"

def contract_risk_score(risks):
    """
    risks: list of strings ["High Risk", "Medium Risk", "Low Risk"]
    returns: percentage score 0-100
    """
    if not risks:
        return 0.0

    # Map string risk levels to numeric scores
    score_map = {"Low Risk": 3, "Medium Risk": 6, "High Risk": 10}

    total = sum(score_map.get(r, 0) for r in risks)
    max_score = len(risks) * 10  # max possible score if all High Risk
    if max_score == 0:
        return 0.0
    return round((total / max_score) * 100, 2)
