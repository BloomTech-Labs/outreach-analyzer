""" Data Validation Schema """
from typing import Optional

from pydantic import BaseModel, Extra, constr, EmailStr


class Outreach(BaseModel):
    name: constr(min_length=3, max_length=128)
    email: EmailStr
    company: constr(min_length=1, max_length=128)
    job_title: constr(min_length=1, max_length=128)
    job_description: constr(min_length=1, max_length=1024)
    key_points_from_resume: constr(min_length=1, max_length=2048)
    outreach: constr(min_length=1, max_length=4096)
    contacts: Optional[constr(max_length=1024)]

    class Config:
        extra = Extra.forbid

class OutreachQuery(BaseModel):
    name: Optional[constr(max_length=128)]
    email: Optional[EmailStr]
    company: Optional[constr(max_length=128)]
    job_title: Optional[constr(max_length=128)]
    job_description: Optional[constr(max_length=1024)]
    key_points_from_resume: Optional[constr(max_length=2048)]
    outreach: Optional[constr(max_length=4096)]
    contacts: Optional[constr(max_length=1024)]

    class Config:
        extra = Extra.forbid

default_outreach = Outreach(
    name="John Doe",
    email="john.doe@gmail.com",
    company="B.A. Consulting",
    job_title="Software Engineer",
    job_description="Experience with Python, Java, C++, and C#.",
    key_points_from_resume="Built a web scraper in Python.",
    outreach="To whom it may concern,\n\nI am interested in the Software Engineer position at B.A. Consulting. I have experience with Python, Java, C++, and C#. I built a web scraper in Python./n/nSincerely,\n\nJohn Doe",
    contacts=None
)

default_outreach_query = OutreachQuery(
    name="John Doe",
    email="john.doe@gmail.com",
    company="B.A. Consulting",
    job_title="Software Engineer",
    job_description="Experience with Python, Java, C++, and C#.",
    key_points_from_resume="Built a web scraper in Python.",
    outreach="To whom it may concern,\n\nI am interested in the Software Engineer position at B.A. Consulting. I have experience with Python, Java, C++, and C#. I built a web scraper in Python./n/nSincerely,\n\nJohn Doe",
    contacts=None
)