from flask import Blueprint, render_template, request, session
from utils import helper
from scipy import stats
import pandas as pd


blueprint = Blueprint('twosamplettest', __name__)


@blueprint.route('/two-sample/two-sample-t-test')
def twosamplettest():
    return render_template('two-sample-tests/two-sample-t-test/two-sample-t-test.html')


@blueprint.route('/two-sample/two-sample-t-test', methods=('POST',))
def fileUpload():
    url = 'two-sample-tests/two-sample-t-test/two-sample-t-test.html'
    return helper.fileUploader(blueprint, url)


@blueprint.route('/two-sample/two-sample-t-test/result', methods=('POST',))
def twosamplettestResult():
    variables = request.form.getlist('varcheckbox[]')
    file = session["FilePath"]
    df = pd.read_csv("static/uploads/{}".format(file))
    selectedvars = df[variables].values
    stat, p = stats.ttest_ind(selectedvars[0], selectedvars[1], equal_var=True)
    return render_template('two-sample-tests/two-sample-t-test/two-sample-t-test-result.html', t=stat,
                           p=p)