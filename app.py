from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return f"Api home page documentations"


@app.route("/healthCheck", methods=["GET"])
def healthCheck() -> str:
    return f"Health chek done, api is responding as espected", 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
