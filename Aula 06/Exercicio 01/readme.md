# uma api simples

## Comandos: 

```bash
$ python3.9 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install chalice boto3 botocore 
(.venv) $ chalice new-project simple_api
(.venv) $ cd simple_api && pip freeze > requirements.txt
```

### Deployment

```bash
(.venv) $ chalice deploy --stage dev
```