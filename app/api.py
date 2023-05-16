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
    allow_origins=['https://zapier.com', 'https://zapier.com/'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

db = Database("Outreach")

@API.get("/version", tags=["Version"])
async def api_version():
    """ Returns current API version
    @return: String Version """
    return API.version

@API.get("/read-outreach", tags=["Outreach"])
async def read_outreach(outreach_query: OutreachQuery = default_outreach_query):
    """ 
    Returns array of all matched outreach
    @param outreach_query: OutreachQuery
    @return: Array[Outreach] 
    """
    return db.find()

@API.get("/total", tags=["Outreach"])
async def total():
    """ Returns total number of outreach
    @return: Int """
    return db.count()

@API.get("/total-by-company", tags=["Outreach"])
async def total_by_company():
    """ Returns total number of outreach by company
    @return: Dict """
    return db.count_by_company()

@API.get("/total-by-job-title", tags=["Outreach"])
async def total_by_job_title():
    """ Returns total number of outreach by job title
    @return: Dict """
    return db.count_by_job_title()

@API.get("/total-by-name", tags=["Outreach"])
async def total_by_name():
    """ Returns total number of outreach by name
    @return: Dict """
    return {"data": db.count_by_name()}