import os
import pickle

import boto3
from chalice import Chalice

app = Chalice(app_name='predict_online')


def obter_arquivo_pickle():
    filename_a_salvar = '/tmp/' + os.getenv('PICKLE_FILENAME')
    s3 = boto3.client('s3')
    s3.download_file(
        os.getenv('PICKLE_BUCKETNAME'),
        os.getenv('PICKLE_FILENAME'),
        filename_a_salvar
    )

    objeto_recuperado = None
    with open(filename_a_salvar, 'rb') as fp:
        objeto_recuperado = pickle.load(fp)

    return objeto_recuperado


def do_predict(fitted_model, x1, x2):
    import numpy as np

    X = np.array([x1, x2]).reshape(1, -1)
    result = fitted_model.predict(X)
    return float(result[0])


@app.route('/')
def index():
    """
    Endpoint de teste
    """
    return {'hello': 'world'}


@app.route("/predict", methods=['GET'])
def get_prediction():
    query_string = app.current_request.query_params
    x1 = float(query_string.get('x1', None))
    x2 = float(query_string.get('x2', None))
    if not x1 or not x2:
        return {'message': 'unable to calculate'}

    model = obter_arquivo_pickle()
    result = do_predict(model, x1, x2)

    return {
        'x1': x1,
        'x2': x2,
        'class': result
    }