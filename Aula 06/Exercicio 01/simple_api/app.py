from chalice import Chalice

app = Chalice(app_name='simple_api')


@app.route('/')
def index():
    return {'olá turmas': ['767', '781']}