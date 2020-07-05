from flask import Blueprint, render_template, request, session
from utils import helper
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


blueprint = Blueprint('proportiontest', __name__)


@blueprint.route('/one-sample/proportion-test')
def proportiontest():
    return render_template('one-sample-tests/proportion-test/proportion-test.html')


@blueprint.route('/one-sample/proportion-test', methods=('POST',))
def fileUpload():
    url = 'one-sample-tests/proportion-test/proportion-test.html'
    return helper.fileUploader(blueprint, url)


@blueprint.route('/one-sample/proportion-test/result', methods=('POST',))
def proportiontestResult():
    count = request.form.get('count')
    nob = request.form.get('nob')
    value = request.form.get('value')
    stat, pval = proportions_ztest(float(count), float(nob), float(value))
    return render_template('one-sample-tests/proportion-test/proportion-test-result.html', z=stat, p=pval)
