from flask import Blueprint, render_template, request, session
from utils import helper
from scipy.stats import anderson
import pandas as pd


blueprint = Blueprint('andersondarling', __name__)


@blueprint.route('/normality/anderson-darling')
def andersondarlingtest():
    return render_template('normality/anderson-darling/anderson-darling.html')


@blueprint.route('/normality/anderson-darling', methods=('POST',))
def fileUpload():
    url = 'normality/anderson-darling/anderson-darling.html'
    return helper.fileUploader(blueprint, url)


@blueprint.route('/normality/anderson-darling-test/result', methods=('POST',))
def andersondarlingtestResult():
    variables = request.form.getlist('varcheckbox[]')
    file = session["FilePath"]
    df = pd.read_csv("static/uploads/{}".format(file))
    selectedvars = df[variables].values
    result = anderson(selectedvars[0])
    stat = result.statistic
    for i in range(len(result.critical_values)):
        sl, cv = result.significance_level[i], result.critical_values[i]
    return render_template('/normality/anderson-darling/anderson-darling-result.html', sl = sl, cv = cv,
                           stat=stat)
