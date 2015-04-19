wget -nc https://bootstrap.pypa.io/get-pip.py
python get-pip.py --user
pip install --user virtualenv
virtualenv venv
. venv/bin/activate
pip install --user flask
pip install --user ming
