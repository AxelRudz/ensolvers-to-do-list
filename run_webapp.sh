. venv/bin/activate
pip install -r requirements.txt
export DB_HOST=localhost
export DB_USER=axelrudz
export DB_PASS=axelrudz123
export DB_NAME=axelrudz_DB
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
