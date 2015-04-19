wget https://bootstrap.pypa.io/ez_setup.py -O - | python
easy_install pip
pip install virtualenv
virtualenv venv
. venv/bin/activate
pip install flask
pip install ming
