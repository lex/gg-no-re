wget https://bootstrap.pypa.io/get-pip.py -O - | python - --user
python -m pip install --user virtualenv
python -m virtualenv venv
. venv/bin/activate
python -m pip install --user flask
python -m pip install --user ming
