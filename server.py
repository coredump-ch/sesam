from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/open', methods=['POST'])
def open():
    email = request.form['email']
    password = request.form['password']
    return 'OPENING for %s / %s' % (email, password)


if __name__ == "__main__":
    app.run(debug=True)
