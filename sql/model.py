from sql.connection import engine, Base

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

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

    def __repr__(self):
        return f"<Jobs id: {self.jobid}, jobTitle: {self.jobtitle}, salary: {self.salary}, currency: {self.currency}>"

# create Table
Base.metadata.create_all(bind=engine)