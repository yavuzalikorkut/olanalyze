from flask import Blueprint, render_template, request, session
from utils import helper
from scipy.stats import shapiro
import pandas as pd


blueprint = Blueprint('shapirowilk', __name__)


@blueprint.route('/normality/shapiro-wilk-test')
def shapirowilktest():
    return render_template('normality/shapiro-wilk-test/shapiro-wilk-test.html')


@blueprint.route('/normality/shapiro-wilk-test', methods=('POST',))
def fileUpload():
    url = '/normality/shapiro-wilk-test/shapiro-wilk-test.html'
    return helper.fileUploader(blueprint, url)


@blueprint.route('/normality/shapiro-wilk-test/result', methods=('POST',))
def shapirowilktestResult():
    variables = request.form.getlist('varcheckbox[]')
    file = session["FilePath"]
    df = pd.read_csv("static/uploads/{}".format(file))
    selectedvars = df[variables].values
    w, p = shapiro(selectedvars)
    return render_template('/normality/shapiro-wilk-test/shapiro-wilk-test-result.html', w=w,
                           p=p)

