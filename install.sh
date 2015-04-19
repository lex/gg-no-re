wget https://bootstrap.pypa.io/get-pip.py -O - | python - --user
python -m pip install virtualenv
virtualenv venv
. venv/bin/activate
python -m pip install flask
python -m pip install ming
