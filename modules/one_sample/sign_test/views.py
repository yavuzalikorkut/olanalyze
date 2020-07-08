from flask import Blueprint, render_template, request, session
from utils import helper
from scipy import stats
import pandas as pd
import numpy as np


blueprint = Blueprint('signtest', __name__)


@blueprint.route('/one-sample/sign-test')
def ttest():
    return render_template('one-sample-tests/sign-test/sign-test.html')


@blueprint.route('/one-sample/sign-test', methods=('POST',))
def fileUpload():
    url = 'one-sample-tests/sign-test/sign-test.html'
    return helper.fileUploader(blueprint, url)


@blueprint.route('/one-sample/sign-test/result', methods=('POST',))
def signtestResult():
    variable = request.form.getlist('varcheckbox[]')
    popmean = request.form.get('popmeansigntest')
    checkval = pd.to_numeric(popmean)
    file = session["FilePath"]
    df = pd.read_csv("static/uploads/{}".format(file))
    selectedvars = df[variable].values
    ini_array1 = np.array(selectedvars)
    onedimensional = ini_array1.flatten()
    t, p = stats.wilcoxon(onedimensional-checkval)
    return render_template('one-sample-tests/sign-test/sign-test-result.html', t=t, p=p)
