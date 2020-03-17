from flask import Blueprint, render_template
from utils import helper

blueprint = Blueprint('ttest', __name__)


@blueprint.route('/one-sample/t-test')
def ttest():
    return render_template('one-sample-tests/t-test.html', task="fileupload")


@blueprint.route('/one-sample/t-test', methods=('POST',))
def file_upload():
    return helper.fileUploader(blueprint)


# def selected_variables():
# pass