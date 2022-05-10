import os
import pickle

import boto3
from chalice import Chalice

app = Chalice(app_name='read_user_data')

# Obter arquivo do s3
def obter_arquivo_pickle():
    _filename_a_salvar = '/tmp/{}'.format(os.getenv('PICKLE_FILENAME'))
    s3 = boto3.client('s3').download_file(
        os.getenv('BUCKET_NAME'),
        os.getenv('PICKLE_FILENAME'),
        _filename_a_salvar
    )   

    _objeto_recuperado = None
    with open(_filename_a_salvar, 'rb') as fp:
        _objeto_recuperado = pickle.load(fp)
    return _objeto_recuperado


def do_predict(fitted_model, x1, x2):
    import numpy as np

    X = np.array([x1,x2]).reshape(1, -1)

    print(x1, type(x1), x2, type(x2))

    result = fitted_model.predict(X)

    print(result[0], type(result[0]))

    return float(result[0])


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/predict', methods=['GET'])
def get_prediction():
    model = obter_arquivo_pickle()
    
    query_string = app.current_request.query_params
    x1 = float(query_string.get('x1', None))
    x2 = float(query_string.get('x2', None))
    if not x1 or not x2:
        return {
            "message": "Unable to calculate"
        }
    
    result = do_predict(model, x1, x2)
    
    return {
        'x1': x1,
        'x2': x2,
        'class': result
    }


@app.route('/predict_post', methods=['POST'])
def get_prediction_via_post():
    model = obter_arquivo_pickle()

    json_body = app.current_request.json_body
    
    query_string = app.current_request.query_params
    x1 = float(query_string.get('x1', None))
    x2 = float(query_string.get('x2', None))
    if not x1 or not x2:
        return {
            "message": "Unable to calculate"
        }

    ## Colocar aqui o codigo do Rodrigo, para obter os dados. 
    result = do_predict(model, x1, x2)

    return {
        'x1': x1,
        'x2': x2,
        'class': result
    }
