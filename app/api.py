from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Database

API = FastAPI(
    title="Outreach Analyzer",
    version="0.0.3",
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
async def read_outreach():
    """ 
    Returns array of all matched outreach, if empty returns all
    documents in the collection
    @return: Array[Outreach] 
    """
    return db.find()


@API.get("/total", tags=["Outreach"])
async def total():
    """ Returns total number of outreaches
    @return: Int """
    return db.count()


@API.get("/total-by-{field}", tags=["Outreach"])
async def total_by_company(field: str):
    """ Returns total number of outreach by field
    @return: Dict """
    return db.count_by_field(field)


@API.get("/count-by-{field}-for-previous-week", tags=["Outreach"])
async def previous_week_count_by_field(field: str):
    """ Returns the total number of outreach by name for the
    past 7 days at the time of analysis
    @return: Dict"""
    return db.count_by_field_previous_week(field)
