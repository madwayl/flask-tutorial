from flask import render_template, jsonify, request, redirect, flash, url_for

from app import app, getJobsFromTable, onUpdateDataBaseFromForm # custom
from app.login import LoginForm

##############
# Main route #
##############

@app.route("/")
@app.route("/index")
def index():
    JOBS = getJobsFromTable()

    form = LoginForm()
    
    # print(JOBS)
    return render_template('home.html', name='Careers', jobs=JOBS, form=form)

########################
# JobApplication route #
########################

@app.route("/job/<id>")
def index_job(id):
    form = LoginForm()
    JOBS = [row.column_as_dict() for row in getJobsFromTable(id)][0]
    if len(JOBS) == 0:
        return "Not Found", 404
    # print(JOBS)
    return render_template('jobpage.html', jobs=JOBS, form=form)

@app.route("/job/<id>/apply", methods=['post'])
def apply_job(id):
    data = request.form
    JOBS = [row.column_as_dict() for row in getJobsFromTable(id)][0]

    if not onUpdateDataBaseFromForm(data, id):
        return "Bad Request", 400
    
    return render_template('applicationsubmitted.html', application=data, jobs=JOBS, form=LoginForm())

###############
# Login route #
###############

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): # works only on POST
        flash('Logged As {}'.format(
            form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    flash('None')
    return redirect(url_for('index'))

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