from flask import Blueprint, render_template, request, session
from utils import helper
from scipy import stats
import pandas as pd


blueprint = Blueprint('binomial', __name__)


@blueprint.route('/one-sample/binomial-test')
def binomialtest():
    return render_template('one-sample-tests/binomial-test/binomial-test.html')


@blueprint.route('/one-sample/binomial-test', methods=('POST',))
def fileUpload():
    url = 'one-sample-tests/binomial-test/binomial-test.html'
    return helper.fileUploader(blueprint, url)


@blueprint.route('/one-sample/binomial-test/result', methods=('POST',))
def binomialtestResult():
    variable = request.form.getlist('varcheckbox')
    file = session["FilePath"]
    df = pd.read_csv("static/uploads/{}".format(file))
    selectedvars = df[variable].shape
    x, n, p = 3, 15, 0.1
    t = stats.binom_test(x, n, p)
    return render_template('one-sample-tests/binomial-test/binomial-test-result.html', t=t)
