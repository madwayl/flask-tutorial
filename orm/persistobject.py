from sqlalchemy.orm import Session
from sqlalchemy import select

from orm.connection import engine
from orm.model import Jobs

# setup Session
session = Session(engine)

JOBS = [
        Jobs(
            jobtitle = "System Administrator",
            salary = "123000",
            currency = "INR",
            jobresponsibilities = "tandard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also",
            jobrequirements = "5 years",
            joblocation = "Remote"
        ),
        Jobs(
            jobtitle = "Frontend Developer",
            salary = "129000",
            currency = "INR",
            jobresponsibilities = "tandard dummy text ever since the 1500s, when an unknown printer took a gasdfsfas afs fas sdf not only five centuries, but also",
            jobrequirements = "2 years",
            joblocation = "Remote"
        ),
        Jobs(
            jobtitle = "Backend Developer",
            salary = "139000",
            currency = "INR",
            jobresponsibilities = "tandard dummy text ever since the 1500s, when an unknown printer took a gasd pe specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, fsfas afs fas sdf not only five centuries, but also",
            jobrequirements = "3 years",
            joblocation = "Remote"
        ),
        Jobs(
            jobtitle = "Accountant",
            salary = "109000",
            currency = "INR",
            jobresponsibilities = "tandard dummy text ever since the 1500s, when an unkn asdfk a g maining essentially unchanged. It was popularised in the 1960s with the release of Le asdfsfas afs fas sdf not only five centuries, but also",
            jobrequirements = "1 year",
            joblocation = "Mumbai, India"
        ),
        Jobs(
            jobtitle = "Data Scientist",
            salary = "199000",
            currency = "INR",
            jobresponsibilities = "tandard dummy text ever since the 1500s, when an unkn asdfk a g maining essentially unchanged. It was popularised in the 1960s with the release of Le taining Lorem Ipsum passages, and more recently with desktop publishing software li afs fas sdf not only five centuries, but also",
            jobrequirements = "3 years",
            joblocation = "Bengaluru, India"
        ),
        Jobs(
            jobtitle = "Data Engineer",
            salary = "299000",
            currency = "INR",
            jobresponsibilities = "tandard dummy text ever since the 1500s, when an unkn asdfk a g maining essenleap into electronic typesetting, remaining taining Lorem Ipsum passages, and more recently with desktop publishing software li afs fas sdf not only five centuries, but also",
            jobrequirements = "5 years",
            joblocation = "Bengaluru, India"
        )
    ]

# session.add_all(JOBS)

def removeDuplicateInsertion(query, session, compareByVal):
    if len(query) == 0:
        return session
    func = lambda row: row.__getattribute__(compareByVal)
    table_map = map(func, query)
    uniqueSession = [
                        job for job in session 
                        if job.__getattribute__(compareByVal) not in table_map
                    ]
    return uniqueSession

allJobTitleFromQuery = list(session.query(Jobs))
allJobTitleInSession = JOBS

uniqueList = removeDuplicateInsertion(allJobTitleFromQuery, allJobTitleInSession, 'jobtitle')

if len(uniqueList) == 0:
    print('none committed')
    session.rollback()
else:
    session.rollback()
    session.add_all(uniqueList)
    session.commit()
    print('committed rows:', uniqueList)