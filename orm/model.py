from orm.connection import engine, Base

from sqlalchemy.types import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, inspect

from typing import List
from datetime import datetime

# Reference Table
class Jobs(Base):
    __tablename__ = 'jobs'
    jobid : Mapped[int] = mapped_column('id', primary_key=True, nullable=False)
    jobtitle : Mapped[str] = mapped_column('jobTitle', String(30), nullable=False)
    salary : Mapped[int] = mapped_column('salary', Integer)
    currency : Mapped[str] = mapped_column('currency', String(3))
    jobresponsibilities: Mapped[str] = mapped_column('jobResponsibilities', String(3200))
    jobrequirements: Mapped[str] = mapped_column('jobRequirements', String(3000))
    joblocation: Mapped[str] = mapped_column('jobLocation', String(30))
    applications: Mapped[List["Applications"]] = relationship()

    def __repr__(self):
        return f"<Job id: {self.jobid}, jobTitle: {self.jobtitle}, salary: {self.salary}, currency: {self.currency}>"
    
    def column_as_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

class Applications(Base):
    __tablename__ = 'applications'
    applicationid : Mapped[int] = mapped_column('id', primary_key=True, nullable=False)
    jobid : Mapped[int] = mapped_column(Integer, ForeignKey("jobs.id"))
    fullname : Mapped[str] = mapped_column(String(30))
    email : Mapped[str] = mapped_column(String(30))
    linkedin_url : Mapped[str] = mapped_column(String(60))
    resume_url : Mapped[str] = mapped_column(String(60))
    work_experience : Mapped[str] = mapped_column(String(300))
    created_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.now(), onupdate=datetime.now())

    def __repr__(self):
        return f"<Application id: {self.applicationid}, jobid: {self.jobid}, email: {self.email}>"

# create Table
Base.metadata.create_all(bind=engine)