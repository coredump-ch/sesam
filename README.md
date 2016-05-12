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

## Configuration variables

The server can be configured using the following env variables:

- `OPENDOOR_PATH`: Path to the [opendoor](./opendoor/) binary.
- `UUID`: The website will be mounted on this value (ideally an UUID).
  Example: `UUID=1234` will result in the mount point `/1234/`.
  Default value is `test`.

## Deployment

You can use ``sesam.service`` to deploy sesam using systemd. Don't forget to
adjust paths and env vars!

If you're using that unit file, you can use the following command to view the logs:

    journalctl -f _SYSTEMD_UNIT=sesam.service
