from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Database
from app.validation import Outreach, OutreachQuery, default_outreach_query, default_outreach


API = FastAPI(
    title="Outreach Analyzer",
    version="0.0.1",
    docs_url="/",
)

API.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = Database("Outreach")

@API.get("/version", tags=["Version"])
async def api_version():
    """ Returns current API version
    @return: String Version """
    return API.version

@API.get("/read-outreach")
async def read_outreach(outreach_query: OutreachQuery = default_outreach_query):
    """ 
    Returns array of all matched outreach
    @param outreach_query: OutreachQuery
    @return: Array[Outreach] 
    """
    return db.find()