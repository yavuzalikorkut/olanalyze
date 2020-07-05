from flask import Blueprint, render_template, request, session
from utils import helper
from scipy import stats
import pandas as pd


blueprint = Blueprint('normalityks', __name__)


@blueprint.route('/normality/ks-test')
def normalitykstest():
    return render_template('normality/ks-test/ks-test.html')


@blueprint.route('/normality/ks-test', methods=('POST',))
def fileUpload():
    url = 'normality/ks-test/ks-test.html'
    return helper.fileUploader(blueprint, url)


@blueprint.route('/normality/ks-test/result', methods=('POST',))
def normalitykstestResult():
    variables = request.form.getlist('varcheckbox[]')
    file = session["FilePath"]
    df = pd.read_csv("static/uploads/{}".format(file))
    selectedvars = df[variables].values
    stat, p = stats.kstest(selectedvars[0], 'norm')
    return render_template('/normality/ks-test/ks-test-result.html', t=stat,
                           p=p)

