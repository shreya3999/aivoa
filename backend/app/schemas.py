from pydantic import BaseModel
from typing import Optional
class ComplaintData(Optional):
    complaint_source:Optional[str]=None
    customer_name:Optional[str]=None
    customer_email:Optional[str]=None
    customer_country:Optional[str]=None
    product_name:Optional[str]=None
    product_code:Optional[str]=None
    product_strenght:Optional[str]=None
    batch_number:Optional[str]=None
    manufacturing_date:Optional[str]=None
    expiry_Date:Optional[str]=None
    quantity_Affected:Optional[str]=None
    complaint_type:Optional[str]=None
    complaint_date:Optional[str]=None
    detailed_complaint_Description:Optional[str]=None
    inital_severity:Optional[str]=None
    priority:Optional[str]=None
    risk_level:Optional[str]=None
    risk_reason:Optional[str]=None
    recommendations:Optional[str]=None
    status:Optional[str]="Open"