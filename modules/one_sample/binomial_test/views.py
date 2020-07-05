<<<<<<< HEAD
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
    x = request.form.get('x')
    n = request.form.get('n')
    p = request.form.get('p')
    pvalue = stats.binom_test(int(x), int(n), float(p))
    return render_template('one-sample-tests/binomial-test/binomial-test-result.html', p=pvalue)
=======
>>>>>>> parent of ebdaec7... add one sample binomial test
