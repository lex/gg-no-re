wget -nc https://bootstrap.pypa.io/get-pip.py
python get-pip.py --user
pip install virtualenv
virtualenv venv
. venv/bin/activate
pip install flask
pip install ming
