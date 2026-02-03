
# Pseudo-LLM wrapper (plug GPT-4 / Claude here)

def explain_clause_simple(clause):
    return (
        "This clause defines responsibilities or restrictions. "
        "It may impact your business financially or operationally."
    )

def generate_summary(contract_type, risk_score):
    return f"""
    This is a {contract_type}.
    Overall risk score: {risk_score}%.
    Higher risk clauses should be reviewed by a legal professional.
    """
