from chalice import Chalice

app = Chalice(app_name='read_user_data')


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/predict', methods=['GET'])
def get_prediction():
    query_string = app.current_request.query_params

    return {
        'x1': query_string.get('x1', 'not informed'),
        'x2': query_string.get('x2', 'not informed'),
        'class': 'NotImplemented'
    }


@app.route('/predict_post', methods=['POST'])
def get_prediction_via_post():
    json_body = app.current_request.json_body

    return {
        'x1': json_body.get('x1', 'not informed'),
        'x2': json_body.get('x2', 'not informed'),
        'class': 'NotImplemented'
    }