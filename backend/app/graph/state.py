from typing import TypedDict,Optional
class ComplaintState(TypedDict):
    #input
    raw_text:str

    #complaint_identification
    complaint_source:str

    #customer
    customer_name:str
    customer_email:str
    customer_country:str

    #product
    product_name:Optional[str]
    product_code:Optional[str]
    product_strenght:Optional[str]
    batch_number:Optional[str]
    manufacturing_date:Optional[str]
    expiry_Date:Optional[str]
    quantity_Affected:Optional[str]

    #complaint

    complaint_type:Optional[str]
    complaint_date:Optional[str]
    detailed_complaint_Description:Optional[str]

    #initial_assement

    inital_severity:Optional[str]
    priority:Optional[str]

    #ai_risk

    risk_level:Optional[str]
    risk_reason:Optional[str]

    #ai_recommendation

    recommendations:Optional[str]
    status:Optional[str]
