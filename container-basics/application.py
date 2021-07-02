import os

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    greeting = os.environ.get("GREETING", "Hello Universe.")
    return greeting
    #return "Hello World! - Hello Cloud Computing"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
