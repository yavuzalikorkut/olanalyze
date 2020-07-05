from flask import Blueprint, render_template, request, session
from utils import helper
from scipy.stats import mannwhitneyu
import pandas as pd


blueprint = Blueprint('mannwhitneyu', __name__)


@blueprint.route('/two-sample/mann-whitney-u-test')
def mannwhitneyutest():
    return render_template('two-sample-tests/mann-whitney-u-test/mann-whitney-u-test.html')


@blueprint.route('/two-sample/mann-whitney-u-test', methods=('POST',))
def fileUpload():
    url = 'two-sample-tests/mann-whitney-u-test/mann-whitney-u-test.html'
    return helper.fileUploader(blueprint, url)


@blueprint.route('/two-sample/mann-whitney-u-test/result', methods=('POST',))
def mannwhitneyutestResult():
    variables = request.form.getlist('varcheckbox[]')
    file = session["FilePath"]
    df = pd.read_csv("static/uploads/{}".format(file))
    selectedvars = df[variables].values
    ''' print(selectedvars) '''
    stat, p = mannwhitneyu(selectedvars[0], selectedvars[1])
    return render_template('two-sample-tests/mann-whitney-u-test/mann-whitney-u-test-result.html', t=stat,
                           p=p)