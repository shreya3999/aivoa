from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)


from app.database import (
    Base,
    engine
)


from app.api.complaints import (
    router
)


# =====================================================
# Create Database Tables
# =====================================================

Base.metadata.create_all(
    bind=engine
)


# =====================================================
# FastAPI Application
# =====================================================

app = FastAPI(

    title=
        "AIVOA AI Complaint Management System",

    description=
        "AI-powered pharmaceutical customer complaint management system",

    version="1.0.0"

)


# =====================================================
# CORS
# =====================================================

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


# =====================================================
# Routes
# =====================================================

app.include_router(
    router
)


# =====================================================
# Root
# =====================================================

@app.get("/")
def root():

    return {

        "message":
            "AIVOA Complaint Management API",

        "status":
            "running"

    }