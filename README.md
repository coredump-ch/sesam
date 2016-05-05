# Sesam

Unser Türöffnungssystem.

## Requirements

- Python 3
- Flask

## Dev setup

    $ python3 -m venv VIRTUAL
    $ . VIRTUAL/bin/activate
    $ pip install -r requirements.txt
    $ python3 server.py
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

## Credentials

Die Credentials müssen als `credentials.txt` Textdatei in folgendem Format im
Hauptordner liegen:

    email1@example.com: password
    email2@example.com: p@ssw0rd
    ...
