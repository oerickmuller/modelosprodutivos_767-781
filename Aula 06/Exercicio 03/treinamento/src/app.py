import pickle
import numpy as np
from flask import Flask, request

def load_model():
    with open('artifacts/model.pickle' , 'rb') as f:
        return pickle.load(f)

app = Flask(__name__)

model = load_model()


@app.route('/')
def main():
    return "Backend rodando"

@app.route('/predict')
def predict():
    try:
        # Usando somente as duas primeiras features do dataset do iris
        x1 = request.args.get('x1')
        x2 = request.args.get('x2')
        if None in [x1, x2]:
            return "Invalid query parameters"
            
        X = np.array([x1,x2]).reshape(1, -1)
        print(X.shape)
        result = model.predict(X)
        return f"Entradas: x1:{x1} x2:{x2} Classe: {result}"

    except Exception as e:
        print(e)
        return "Ocorreu um problema :("   
