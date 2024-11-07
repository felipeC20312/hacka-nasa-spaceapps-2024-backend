import json
from flask import Flask, request, jsonify
from flasgger import Swagger
from modules.consultajson import manipula_json
from modules.agriculture_forecast import process_agricultural_forecasting

app = Flask(__name__)
swagger = Swagger(app)


@app.route("/")
def home():
    """Página inicial da API
    ---
    responses:
      200:
        description: Retorna a página inicial da API
        schema:
          type: string
          example: "Api home page documentations"
    """
    return "Api home page documentations"


@app.route("/healthCheck", methods=["GET"])
def healthCheck():
    """Verificação de Saúde da API
    ---
    responses:
      200:
        description: Confirma que a API está respondendo como esperado
        schema:
          type: string
          example: "Health check done, api is responding as expected"
    """
    return "Health check done, api is responding as expected", 200


@app.route("/manipulaJson", methods=["POST"])
def manipuloJson():
    """Manipula dados JSON recebidos
    ---
    parameters:
      - in: body
        name: dados_json
        description: JSON com dados a serem manipulados
        required: true
        schema:
          type: object
    responses:
      200:
        description: JSON manipulado
        schema:
          type: string
    """
    dados_json = request.get_json()
    return manipula_json(json.dumps(dados_json))


@app.route("/process_agricultural_forecasting", methods=["POST"])
def processAgriculturalForecasting():
    """Processa a previsão agrícola
    ---
    parameters:
      - in: body
        name: data_json
        description: JSON contendo dados para a previsão agrícola
        required: true
        schema:
          type: object
          properties:
            crop:
              type: array
              items:
                type: string
              example: ["corn", "Soybean"]
            size:
              type: string
              example: "1 a 3 hectars"
            location:
              type: object
              properties:
                latitude:
                  type: number
                  example: -16.686072
                longitude:
                  type: number
                  example: -49.262533
    responses:
      200:
        description: Resultados da previsão agrícola
        schema:
          type: string
    """
    data_json = request.get_json()
    return process_agricultural_forecasting(data_json)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
