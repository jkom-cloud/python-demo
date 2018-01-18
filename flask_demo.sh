./venv/bin/python -m pip install -r requirements.txt
FLASK_APP=flask_demo.py ./venv/bin/flask run -h $HOST -p $PORT
