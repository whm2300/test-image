from flask import Flask

import socket
import os

app = Flask(__name__)


@app.route('/')
def hello():
    html = "<h3>Hello {name} ! </h3>" \
        "<b> Hostname:</b> {hostname}</br>"
    host = socket.gethostname()
    return html.format(name=os.getenv("NAME", "WORLD"),
                       hostname=os.getenv("MY_POD_IP", "0.0.0.0"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)