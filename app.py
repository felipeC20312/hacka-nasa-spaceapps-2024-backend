import json
from flask import Flask, request, jsonify
from modules.consultajson import manipula_json

app = Flask(__name__)


@app.route("/")
def home():
    return f"Api home page documentations"


@app.route("/healthCheck", methods=["GET"])
def healthCheck() -> str:
    return f"Health chek done, api is responding as espected", 200


@app.route("/manipulaJson", methods=["POST"])
def manipuloJson() -> str:
    dados_json = request.get_json()
    return manipula_json(json.dumps(dados_json))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
