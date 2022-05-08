import json
import os

import boto3
from chalice import Chalice

app = Chalice(app_name='primeiro_projeto')


@app.route('/')
def index():
    return {
        'mensagem': 'ola, turmas', 
        'turmas': [767, 781], 
        'bucket_usado': os.getenv('NOME_BUCKET')
    }


@app.route('/ler_json')
def ler_json():
    nome_bucket = os.getenv('NOME_BUCKET')
    nome_arquivo = os.getenv('NOME_ARQUIVO')
    
    s3 = boto3.client('s3')
    destino = '/tmp/arquivo.json'
    s3.download_file(nome_bucket, nome_arquivo, destino) 

    with open(destino, 'r') as fp:
        linhas = fp.readlines()
    
    linhas = ''.join(linhas)
    return json.loads(linhas)   


@app.route('/predict')
def predict_via_querystring():
    query_string = app.current_request.query_params

    x1 = query_string.get('x1', 0)
    x2 = query_string.get('x2', 0)

    return {
        'x1': x1,
        'x2': x2,
        'order': 'NaoImplementado'
    }