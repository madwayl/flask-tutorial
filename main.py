from flask import render_template, jsonify, request

from app import app, getJobsFromTable, onUpdateDataBaseFromForm

##############
# Main route #
##############

@app.route("/")
@app.route("/index")
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

    if not onUpdateDataBaseFromForm(data, id):
        return "Bad Request", 400
    
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