from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Jenkins CI/CD!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
# this is is a simple of Flask application Flask that runs on when8080 and returns a simple message when accessed.
