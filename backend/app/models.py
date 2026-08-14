from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.database import Base


class Complaint(Base):

    __tablename__ = "complaints"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    complaint_number = Column(
        String(100),
        unique=True,
        index=True
    )

    complaint_source = Column(
        String(255)
    )

    customer_name = Column(
        String(255)
    )

    customer_email = Column(
        String(255)
    )

    customer_country = Column(
        String(100)
    )

    product_name = Column(
        String(255)
    )

    product_code = Column(
        String(100)
    )

    product_strength = Column(
        String(255)
    )

    batch_number = Column(
        String(255)
    )

    manufacturing_date = Column(
        String(100)
    )

    expiry_date = Column(
        String(100)
    )

    quantity_affected = Column(
        Integer
    )

    complaint_type = Column(
        String(255)
    )

    complaint_date = Column(
        String(100)
    )

    detailed_complaint_description = Column(
        Text
    )

    initial_severity = Column(
        String(50)
    )

    priority = Column(
        String(50)
    )

    completeness_status = Column(
        String(50)
    )

    missing_fields = Column(
        Text
    )

    risk_level = Column(
        String(50)
    )

    risk_reason = Column(
        Text
    )

    recommendations = Column(
        Text
    )

    status = Column(
        String(100),
        default="Open"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )