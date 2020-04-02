from flask import Blueprint, render_template, request, session
from utils import helper
from scipy import stats
import pandas as pd


blueprint = Blueprint('ttest', __name__)


@blueprint.route('/one-sample/t-test')
def ttest():
    return render_template('one-sample-tests/t-test/t-test.html')


@blueprint.route('/one-sample/t-test', methods=('POST',))
def fileUpload():
    url = 'one-sample-tests/t-test/t-test.html'
    return helper.fileUploader(blueprint, url)


@blueprint.route('/one-sample/t-test/result', methods=('POST',))
def ttestResult(alpha=0.05, alternative='greater'):
    variables = request.form.getlist('varcheckbox')
    popmean = request.form.get('popmean')
    popmeannumeric = pd.to_numeric(popmean)
    file = session["FilePath"]
    df = pd.read_csv("static/uploads/{}".format(file))
    selectedvar = df[variables]
    t, p = stats.ttest_1samp(selectedvar, popmeannumeric)
    h0 = ' '  # define here otherwise unreachable for this scope
    if alternative == 'greater' and (p/2 < alpha) and t > 0:
        h0 = 'Reject Null Hypothesis for greater-than test'
    if alternative == 'less' and (p/2 < alpha) and t < 0:
        h0 = 'Reject Null Hypothesis for less-thane test'
    return render_template('one-sample-tests/t-test/t-test-result.html', h0=h0)
