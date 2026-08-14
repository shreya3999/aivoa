import json
import uuid

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from pypdf import PdfReader


from app.database import get_db

from app.models import Complaint

from app.graph.workflow import workflow


router = APIRouter(

    prefix="/api/complaints",

    tags=["Complaints"]

)


# =====================================================
# ANALYZE COMPLAINT
# =====================================================

@router.post("/analyze")
async def analyze_complaint(

    file: UploadFile = File(...)

):


    contents = await file.read()


    text = ""


    # ---------------------------------------------
    # PDF
    # ---------------------------------------------

    if file.filename.lower().endswith(
        ".pdf"
    ):


        temp_file = (
            "temp_complaint.pdf"
        )


        with open(
            temp_file,
            "wb"
        ) as f:

            f.write(contents)


        reader = PdfReader(
            temp_file
        )


        for page in reader.pages:

            text += (
                page.extract_text()
                or ""
            )


    # ---------------------------------------------
    # TXT
    # ---------------------------------------------

    else:

        try:

            text = contents.decode(
                "utf-8"
            )

        except UnicodeDecodeError:

            raise HTTPException(

                status_code=400,

                detail=
                    "Unsupported file format"

            )


    # ---------------------------------------------
    # Check text
    # ---------------------------------------------

    if not text.strip():

        raise HTTPException(

            status_code=400,

            detail=
                "No text found in document"

        )


    # ---------------------------------------------
    # Initial LangGraph State
    # ---------------------------------------------

    initial_state = {

        "raw_text": text,

        "complaint_source": None,


        "customer_name": None,

        "customer_email": None,

        "customer_country": None,


        "product_name": None,

        "product_code": None,

        "product_strength": None,

        "batch_number": None,

        "manufacturing_date": None,

        "expiry_date": None,

        "quantity_affected": None,


        "complaint_type": None,

        "complaint_date": None,

        "detailed_complaint_description": None,


        "initial_severity": None,

        "priority": None,


        "completeness_status": None,

        "missing_fields": [],


        "risk_level": None,

        "risk_reason": None,


        "recommendations": []

    }


    # ---------------------------------------------
    # Run LangGraph
    # ---------------------------------------------

    result = workflow.invoke(
        initial_state
    )


    # ---------------------------------------------
    # Return result
    # ---------------------------------------------

    return {

        "complaint": {

            "complaint_source":
                result.get(
                    "complaint_source"
                ),


            "customer_name":
                result.get(
                    "customer_name"
                ),

            "customer_email":
                result.get(
                    "customer_email"
                ),

            "customer_country":
                result.get(
                    "customer_country"
                ),


            "product_name":
                result.get(
                    "product_name"
                ),

            "product_code":
                result.get(
                    "product_code"
                ),

            "product_strength":
                result.get(
                    "product_strength"
                ),

            "batch_number":
                result.get(
                    "batch_number"
                ),

            "manufacturing_date":
                result.get(
                    "manufacturing_date"
                ),

            "expiry_date":
                result.get(
                    "expiry_date"
                ),

            "quantity_affected":
                result.get(
                    "quantity_affected"
                ),


            "complaint_type":
                result.get(
                    "complaint_type"
                ),

            "complaint_date":
                result.get(
                    "complaint_date"
                ),

            "detailed_complaint_description":
                result.get(
                    "detailed_complaint_description"
                ),


            "initial_severity":
                result.get(
                    "initial_severity"
                ),

            "priority":
                result.get(
                    "priority"
                )

        },


        "completeness": {

            "status":
                result.get(
                    "completeness_status"
                ),

            "missing_fields":
                result.get(
                    "missing_fields"
                )

        },


        "risk_assessment": {

            "risk_level":
                result.get(
                    "risk_level"
                ),

            "reason":
                result.get(
                    "risk_reason"
                )

        },


        "recommendations":
            result.get(
                "recommendations"
            )

    }


# =====================================================
# SAVE COMPLAINT
# =====================================================

@router.post("")
async def create_complaint(

    complaint_data: dict,

    db: Session = Depends(
        get_db
    )

):


    complaint_number = (

        "CMP-"

        + str(
            uuid.uuid4()
        )[:8].upper()

    )


    complaint = Complaint(

        complaint_number=
            complaint_number,


        complaint_source=
            complaint_data.get(
                "complaint_source"
            ),


        customer_name=
            complaint_data.get(
                "customer_name"
            ),

        customer_email=
            complaint_data.get(
                "customer_email"
            ),

        customer_country=
            complaint_data.get(
                "customer_country"
            ),


        product_name=
            complaint_data.get(
                "product_name"
            ),

        product_code=
            complaint_data.get(
                "product_code"
            ),

        product_strength=
            complaint_data.get(
                "product_strength"
            ),

        batch_number=
            complaint_data.get(
                "batch_number"
            ),

        manufacturing_date=
            complaint_data.get(
                "manufacturing_date"
            ),

        expiry_date=
            complaint_data.get(
                "expiry_date"
            ),

        quantity_affected=
            complaint_data.get(
                "quantity_affected"
            ),


        complaint_type=
            complaint_data.get(
                "complaint_type"
            ),

        complaint_date=
            complaint_data.get(
                "complaint_date"
            ),

        detailed_complaint_description=
            complaint_data.get(
                "detailed_complaint_description"
            ),


        initial_severity=
            complaint_data.get(
                "initial_severity"
            ),

        priority=
            complaint_data.get(
                "priority"
            ),


        completeness_status=
            complaint_data.get(
                "completeness_status"
            ),


        missing_fields=json.dumps(

            complaint_data.get(
                "missing_fields",
                []
            )

        ),


        risk_level=
            complaint_data.get(
                "risk_level"
            ),

        risk_reason=
            complaint_data.get(
                "risk_reason"
            ),


        recommendations=json.dumps(

            complaint_data.get(
                "recommendations",
                []
            )

        ),


        status=
            complaint_data.get(
                "status",
                "Open"
            )

    )


    db.add(
        complaint
    )


    db.commit()


    db.refresh(
        complaint
    )


    return {

        "message":
            "Complaint created successfully",

        "complaint_id":
            complaint.id,

        "complaint_number":
            complaint.complaint_number

    }


# =====================================================
# GET ALL COMPLAINTS
# =====================================================

@router.get("")
def get_complaints(

    db: Session = Depends(
        get_db
    )

):


    complaints = (

        db.query(
            Complaint
        )

        .order_by(
            Complaint.created_at.desc()
        )

        .all()

    )


    return complaints


# =====================================================
# GET ONE COMPLAINT
# =====================================================

@router.get("/{complaint_id}")
def get_complaint(

    complaint_id: int,

    db: Session = Depends(
        get_db
    )

):


    complaint = (

        db.query(
            Complaint
        )

        .filter(
            Complaint.id == complaint_id
        )

        .first()

    )


    if not complaint:

        raise HTTPException(

            status_code=404,

            detail=
                "Complaint not found"

        )


    return complaint