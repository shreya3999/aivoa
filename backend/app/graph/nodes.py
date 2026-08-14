from langchain_groq import ChatGroq
from pydantic import BaseModel
from typing import Optional, List

from app.graph.state import ComplaintState


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


# =====================================================
# STRUCTURED OUTPUT MODELS
# =====================================================

class ComplaintExtraction(BaseModel):
    complaint_source: Optional[str] = None

    customer_name: Optional[str] = None
    customer_email: Optional[str] = None
    customer_country: Optional[str] = None

    product_name: Optional[str] = None
    product_code: Optional[str] = None
    product_strength: Optional[str] = None
    batch_number: Optional[str] = None
    manufacturing_date: Optional[str] = None
    expiry_date: Optional[str] = None
    quantity_affected: Optional[str] = None

    complaint_type: Optional[str] = None
    complaint_date: Optional[str] = None
    detailed_complaint_description: Optional[str] = None

    initial_severity: Optional[str] = None
    priority: Optional[str] = None


class RiskAssessment(BaseModel):
    risk_level: str
    risk_reason: str


class Recommendations(BaseModel):
    recommendations: List[str]


# =====================================================
# NODE 1 - EXTRACT COMPLAINT
# =====================================================

def extract_complaint(state: ComplaintState):

    prompt = f"""
You are an AI assistant working for a pharmaceutical company.

Analyze the following customer complaint and extract the available
information.

COMPLAINT:
{state["raw_text"]}

Rules:

1. Extract only information explicitly present in the complaint.
2. Do not invent information.
3. If information is unavailable, return null.
4. Preserve the meaning of the complaint.
"""

    structured_llm = llm.with_structured_output(
        ComplaintExtraction
    )

    result = structured_llm.invoke(prompt)

    return result.model_dump()


# =====================================================
# NODE 2 - COMPLETENESS CHECKER
# =====================================================

def check_completeness(state: ComplaintState):

    required_fields = [
        "customer_name",
        "product_name",
        "batch_number",
        "complaint_date",
        "detailed_complaint_description"
    ]

    missing = []

    for field in required_fields:

        value = state.get(field)

        if value is None or value == "":
            missing.append(field)

    state["missing_fields"] = missing

    if len(missing) == 0:
        state["completeness_status"] = "complete"
    else:
        state["completeness_status"] = "Incomplete"

    return state


# =====================================================
# NODE 3 - AI RISK ASSESSMENT
# =====================================================

def assess_risk(state: ComplaintState):

    prompt = f"""
You are a pharmaceutical quality risk assessment assistant.

Analyze the following customer complaint.

Product:
{state.get("product_name")}

Product Strength:
{state.get("product_strength")}

Batch:
{state.get("batch_number")}

Complaint Type:
{state.get("complaint_type")}

Description:
{state.get("detailed_complaint_description")}

Quantity:
{state.get("quantity_affected")}

Initial Severity:
{state.get("initial_severity")}

Classify the risk as exactly one of:

low
medium
high
critical

Consider:

- patient safety
- product quality
- product contamination
- packaging defects
- manufacturing issues
- potential batch-wide impact
"""

    structured_llm = llm.with_structured_output(
        RiskAssessment
    )

    result = structured_llm.invoke(prompt)

    state["risk_level"] = result.risk_level
    state["risk_reason"] = result.risk_reason

    return state


# =====================================================
# NODE 4 - GENERATE RECOMMENDATIONS
# =====================================================

def generate_recommendations(
    state: ComplaintState
):

    prompt = f"""
You are a pharmaceutical quality management assistant.

Complaint:

{state.get("detailed_complaint_description")}

Risk Level:

{state.get("risk_level")}

Risk Reason:

{state.get("risk_reason")}

Provide exactly 3 recommended investigation actions.
"""

    structured_llm = llm.with_structured_output(
        Recommendations
    )

    result = structured_llm.invoke(prompt)

    state["recommendations"] = result.recommendations

    return state