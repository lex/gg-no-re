wget https://bootstrap.pypa.io/ez_setup.py -O - | python - --user
easy_install pip
pip install virtualenv
virtualenv venv
. venv/bin/activate
pip install flask
pip install ming
pip install bibtexparser
