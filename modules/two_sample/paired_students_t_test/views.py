from flask import Blueprint, render_template, request, session
from utils import helper
from scipy.stats import ttest_rel
import pandas as pd


blueprint = Blueprint('pairedstudents', __name__)


@blueprint.route('/two-sample/paired-students-t-test')
def pairedstudentsttest():
    return render_template('two-sample-tests/paired-students-t-test/paired-students-t-test.html')


@blueprint.route('/two-sample/paired-students-t-test', methods=('POST',))
def fileUpload():
    url = 'two-sample-tests/paired-students-t-test/paired-students-t-test.html'
    return helper.fileUploader(blueprint, url)


@blueprint.route('/two-sample/paired-students-t-test/result', methods=('POST',))
def pairedstudentsttestResult():
    variables = request.form.getlist('varcheckbox[]')
    file = session["FilePath"]
    df = pd.read_csv("static/uploads/{}".format(file))
    selectedvars = df[variables].values
    stat, p = ttest_rel(selectedvars[0], selectedvars[1])
    return render_template('two-sample-tests/paired-students-t-test/paired-students-t-test-result.html', t=stat,
                           p=p)