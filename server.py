import os
import subprocess

from flask import Flask, request, render_template


app = Flask(__name__)

APP_ROOT = os.environ.get('UUID', 'test')


@app.route('/%s/' % APP_ROOT, methods=['GET'])
def main():
    return render_template('main.html')


@app.route('/%s/' % APP_ROOT, methods=['POST'])
def open():
    email = request.form['email']
    password = request.form['password']
    if check_credentials(email, password):
        trigger()
        return 'Opened', 204
    else:
        return 'Bad credentials', 401


def check_credentials(email, password):
    # TODO: Check credentials
    return True


def trigger():
    """
    Trigger the open door binary.

    This call will block for a few seconds.
    """
    opendoor_path = os.environ.get('OPENDOOR_PATH', 'opendoor')
    subprocess.check_call(opendoor_path)


if __name__ == "__main__":
    app.run(debug=True)
