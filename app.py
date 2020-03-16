from flask import Flask, render_template, request
from utils import helper
# from flask.ext.babel import Babel

app = Flask(__name__)
# app.secret_key = "Flask_File_Upload_Example"
# babel = Babel(app)
# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='Flask_File_Upload_Example',
    LANGUAGES = {
    'en': 'English',
    'tr': 'Turkish'
    }
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


# @babel.localeselector
# def get_locale():
#     return request.accept_languages.best_match(app.config['LANGUAGES'].keys())


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/one-sample')
def onesample():
    page = "onesample"
    return render_template('one-sample.html', page=page)


@app.route('/two-sample')
def twosample():
    page = "twosample"
    return render_template('two-sample.html', page=page)


@app.route('/t-test')
def ttest():
    return render_template('one-sample-tests/t-test.html', task="fileupload")


@app.route('/t-test', methods=['POST'])
def file_upload():
    return helper.fileUploader(app)


def selected_variables():
    pass


if __name__ == '__main__':
    app.run()