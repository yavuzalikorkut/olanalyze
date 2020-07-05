from flask import Blueprint, render_template, request, session
from utils import helper
import numpy as np
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest


blueprint = Blueprint('proportionsz', __name__)


@blueprint.route('/two-sample/proportions-z-test')
def proportionsztest():
    return render_template('two-sample-tests/proportions-z-test/proportions-z-test.html')


@blueprint.route('/two-sample/proportions-z-test', methods=('POST',))
def fileUpload():
    url = 'two-sample-tests/proportions-z-test/proportions-z-test.html'
    return helper.fileUploader(blueprint, url)


@blueprint.route('/two-sample/proportions-z-test/result', methods=('POST',))
def proportionsztestResult():
    count1 = request.form.get('count1')
    count2 = request.form.get('count2')
    nob1 = request.form.get('nob1')
    nob2 = request.form.get('nob2')
    count = np.array([float(count1), float(count2)])
    nobs = np.array([float(nob1), float(nob2)])
    stat, pval = proportions_ztest(count, nobs)
    return render_template('two-sample-tests/proportions-z-test/proportions-z-test-result.html', z=stat,
                           p=pval)
