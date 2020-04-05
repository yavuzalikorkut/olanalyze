from flask import Blueprint, render_template, request, session
from utils import helper
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


blueprint = Blueprint('proportiontest', __name__)


@blueprint.route('/one-sample/proportion-test')
def signtest():
    return render_template('one-sample-tests/proportion-test/proportion-test.html')


@blueprint.route('/one-sample/proportion-test', methods=('POST',))
def fileUpload():
    url = 'one-sample-tests/proportion-test/proportion-test.html'
    return helper.fileUploader(blueprint, url)


@blueprint.route('/one-sample/proportion-test/result', methods=('POST',))
def proportiontestResult():
    count = np.array([5, 12])
    nobs = np.array([83, 99])
    stat, pval = proportions_ztest(count, nobs)
    a = ('{0:0.3f}'.format(pval))
    return render_template('one-sample-tests/proportion-test/proportion-test-result.html', stat=stat, pval=pval)
