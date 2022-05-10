## Comandos

### treinamento

_Digitar apenas o que está **depois** do sinal $_

```
$ python3.8 -m venv .venv_treinamento
$ source .venv_treinamento/bin/activate
(.venv_treinamento) $ pip install -r requirements.txt
(.venv_treinamento) $ python treinamento.py
(.venv_treinamento) $ deactivate
```

### aplicacao

_Digitar apenas o que está **depois** do sinal $_

``` 
$ python3.8 -m venv .venv_aplicacao
$ source .venv_aplicacao/bin/activate
(.venv_aplicacao) $ pip install chalice boto3 botocore
(.venv_aplicacao) $ chalice new-project full_data_analysis
(.venv_aplicacao) $ cd full_data_analysis
(.venv_aplicacao) $ pip freeze > requirements.txt

```