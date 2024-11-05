import json


def manipula_json(dados_json):
    dados = json.loads(dados_json)
    dados["status"] = "processado"
    resultado_json = json.dumps(dados)
    return resultado_json
