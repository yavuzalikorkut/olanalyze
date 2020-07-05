from flask import Blueprint, render_template, request, session
from utils import helper
from scipy import stats
import pandas as pd


blueprint = Blueprint('twosampleks', __name__)


@blueprint.route('/two-sample/two-sample-ks-test')
def twosamplekstest():
    return render_template('two-sample-tests/two-sample-ks-test/two-sample-ks-test.html')


@blueprint.route('/two-sample/two-sample-ks-test', methods=('POST',))
def fileUpload():
    url = 'two-sample-tests/two-sample-ks-test/two-sample-ks-test.html'
    return helper.fileUploader(blueprint, url)


@blueprint.route('/two-sample/two-sample-ks-test/result', methods=('POST',))
def twosamplekstestResult():
    variables = request.form.getlist('varcheckbox[]')
    file = session["FilePath"]
    df = pd.read_csv("static/uploads/{}".format(file))
    selectedvars = df[variables].values
    stat, p = stats.ks_2samp(selectedvars[0], selectedvars[1])
    return render_template('two-sample-tests/two-sample-ks-test/two-sample-ks-test-result.html', t=stat,
                           p=p)