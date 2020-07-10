# Olanalyze

[![GitHub version](https://badge.fury.io/gh/yavuzalikorkut%2Folanalyze.svg)](https://badge.fury.io/gh/yavuzalikorkut%2Folanalyze)
[![PyPI](https://img.shields.io/pypi/pyversions/scipy)](https://pypi.org/project/scipy/)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/yavuzalikorkut/olanalyze)

[Olanalyze](https://olanalyze.herokuapp.com/) is a web app that will enable statistical hypothesis testing. This app has been developed for correct test selection with flow chart. It based on [flask](https://flask.palletsprojects.com/en/1.1.x/) and uses [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html) for statistical tests.

## Installation

First install virtual environment for your machine. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install virtual environment.

```bash
pip3 install virtualenv 
```

Clone the repository

```bash
git clone https://github.com/yavuzalikorkut/olanalyze.git
cd olanalyze
```

Create a folder for virtual environment

```bash
mkdir venv
cd venv
virtualenv myvenv
```
Activate your virtual environment
```bash
source myenv/bin/activate
```
Install requirements
```bash
(myvenv) pip3 install -r requirements.txt
```

## Running project locally

You can use development server

```bash
 (myvenv) $ export FLASK_APP=wsgi.py
 (myvenv) $ flask run
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)