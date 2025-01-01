from flask import Flask, render_template, jsonify, request
from orm.persistobject import session
from orm.model import Jobs

app = Flask(__name__)

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

##############
# Main route #
##############

@app.route("/")
def index():
    JOBS = getJobsFromTable()
    # print(JOBS)
    return render_template('home.html', name='Careers', jobs=JOBS)

########################
# JobApplication route #
########################

@app.route("/job/<id>")
def index_job(id):
    JOBS = [row.column_as_dict() for row in getJobsFromTable(id)][0]
    if len(JOBS) == 0:
        return "Not Found", 404
    # print(JOBS)
    return render_template('jobpage.html', jobs=JOBS)

@app.route("/job/<id>/apply", methods=['post'])
def apply_job(id):
    data = request.form
    JOBS = [row.column_as_dict() for row in getJobsFromTable(id)][0]
    return render_template('applicationsubmitted.html', application=data, jobs=JOBS)

#################
# All API route #
#################

@app.route("/api/jobs")
def list_jobs():
    JOBS = [row.column_as_dict() for row in getJobsFromTable()]
    return jsonify(JOBS)

@app.route("/api/jobs/<id>")
def list_job_by_id(id):
    JOBS = [row.column_as_dict() for row in getJobsFromTable(id)]
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)