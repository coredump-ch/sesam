import os
import subprocess
import logging

from flask import Flask, request, render_template


app = Flask(__name__)
logger = logging.getLogger('sesam')

APP_ROOT = os.environ.get('UUID', 'test')


@app.route('/%s/' % APP_ROOT, methods=['GET'])
def main():
    return render_template('main.html')


@app.route('/%s/' % APP_ROOT, methods=['POST'])
def process():
    email = request.form['email']
    password = request.form['password']
    if credentials_valid(email, password):
        trigger()
        return 'Opened', 204
    else:
        return 'Bad credentials', 401


def credentials_valid(email, password):
    if not email or not password:
        logger.error('Either email or password were not defined')
        return False
    if not os.path.exists('credentials.txt'):
        logger.error('File credentials.txt does not exist')
        return False
    if not os.path.isfile('credentials.txt'):
        logger.error('Path credentials.txt is not a file')
        return False
    with open('credentials.txt', 'r') as f:
        lines = [
            map(lambda x: x.strip(), line.split(':'))
            for line in f
        ]
        data = dict(lines)
    return data.get(email) == password


def trigger():
    """
    Trigger the open door binary.

    This call will block for a few seconds.
    """
    opendoor_path = os.environ.get('OPENDOOR_PATH', 'opendoor')
    subprocess.check_call(opendoor_path)


if __name__ == "__main__":
    app.run(debug=False)
