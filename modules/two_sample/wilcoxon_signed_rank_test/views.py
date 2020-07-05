from flask import Blueprint, render_template, request, session
from utils import helper
from scipy.stats import wilcoxon
import pandas as pd


blueprint = Blueprint('wilcoxonsignedrank', __name__)


@blueprint.route('/two-sample/wilcoxon-signed-rank-test')
def wilcoxonsignedranktest():
    return render_template('two-sample-tests/wilcoxon-signed-rank-test/wilcoxon-signed-rank-test.html')


@blueprint.route('/two-sample/wilcoxon-signed-rank-test', methods=('POST',))
def fileUpload():
    url = 'two-sample-tests/wilcoxon-signed-rank-test/wilcoxon-signed-rank-test.html'
    return helper.fileUploader(blueprint, url)


@blueprint.route('/two-sample/wilcoxon-signed-rank-test/result', methods=('POST',))
def wilcoxonsignedranktestResult():
    variables = request.form.getlist('varcheckbox[]')
    ''' print(variables) '''
    file = session["FilePath"]
    df = pd.read_csv("static/uploads/{}".format(file))
    selectedvars = df[variables].values
    ''' print(selectedvars) '''
    stat, p = wilcoxon(selectedvars[0], selectedvars[1])
    return render_template('two-sample-tests/wilcoxon-signed-rank-test/wilcoxon-signed-rank-test-result.html', t=stat, p=p)

