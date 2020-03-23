import os
from flask import request, redirect, flash, render_template
from werkzeug.utils import secure_filename
import uuid
import pandas as pd

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['csv'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def fileUploader(app):
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No file selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = str(uuid.uuid4()) + ".csv"
        # session a kaydedince session["FilePath"] = filename
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        flash('File successfully uploaded')
        df = pd.read_csv("/Users/yavuzalikorkutustbas/PycharmProjects/stata-onl/static/uploads/{}".format(filename))
        table = df.head()
        tablelist = table.values.tolist()
        content = {'f': tablelist}
        columns = df.columns
        return render_template('one-sample-tests/t-test.html', task="selected", columns=columns, tablelist=content)
    else:
        flash('Allowed file types is csv')
        return redirect(request.url)


# def fileName():
#     file = request.files['file']
#     fname = file.filename
#     return fname
