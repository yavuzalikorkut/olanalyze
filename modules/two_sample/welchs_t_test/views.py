from flask import Blueprint, render_template, request, session
from utils import helper
from scipy import stats
import pandas as pd


blueprint = Blueprint('welchsttest', __name__)


@blueprint.route('/two-sample/welchs-t-test')
def welchsttest():
    return render_template('two-sample-tests/welchs-t-test/welchs-t-test.html')


@blueprint.route('/two-sample/welchs-t-test', methods=('POST',))
def fileUpload():
    url = 'two-sample-tests/welchs-t-test/welchs-t-test.html'
    return helper.fileUploader(blueprint, url)


@blueprint.route('/two-sample/welchs-t-test/result', methods=('POST',))
def welchsttestResult():
    variables = request.form.getlist('varcheckbox[]')
    file = session["FilePath"]
    df = pd.read_csv("static/uploads/{}".format(file))
    selectedvars = df[variables].values
    stat, p = stats.ttest_ind(selectedvars[0], selectedvars[1], equal_var=False)
    return render_template('two-sample-tests/welchs-t-test/welchs-t-test-result.html', t=stat,
                           p=p)