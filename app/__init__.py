from flask import Flask
from config import Config

from app.orm.persistobject import session
from app.orm.model import Jobs, Applications

app = Flask(__name__)
app.config.from_object(Config)

# JOBS = [
#     { 'id': 1, 'title': 'Frontend Engineer', 'location': 'Remote', 'salary': 'Rs. 22,00,000' },
#     { 'id': 2, 'title': 'Backtend Engineer', 'location': 'Remote', 'salary': 'Rs. 22,00,000' },
#     { 'id': 3, 'title': 'Devend Engineer', 'location': 'Remote', 'salary': 'Rs. 15,00,000' },
#     { 'id': 3, 'title': 'IT Engineer', 'location': 'In-Office, San Francisco', 'salary': 'Rs. 13,00,000' },
# ]

def getJobsFromTable(id=None):
    if not id:
        return list(session.query(Jobs))
    return list(session.query(Jobs).where(Jobs.jobid == id))

def onUpdateDataBaseFromForm(application:dict, jobid):
    if len(list(session.query(Jobs).filter_by(jobid=jobid))) == 0:
        return False
    
    print(application)

    query_check = session.query(Applications).\
                    filter_by(jobid=jobid).\
                    filter_by(email=application['email'])

    if len(list(query_check)) == 0:
        applicaitonFormSub = Applications(
            jobid = jobid,
            fullname = application['fullname'],
            email = application['email'],
            linkedin_url = application['linkedinURL'],
            resume_url = application['ResumeURL'],
            work_experience = application['workExperience']
        )
        session.add(applicaitonFormSub)
    else:
        query_check.update({
            Applications.fullname: application['fullname'],
            Applications.linkedin_url: application['linkedinURL'],
            Applications.resume_url: application['ResumeURL'],
            Applications.work_experience: application['workExperience']
        })

    session.commit()

    return True

from app import routes

###########
# Run App #
###########

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)