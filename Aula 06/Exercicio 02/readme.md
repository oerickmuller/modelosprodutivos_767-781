# obtendo dados dos usuários

## Comandos

### Pre install

```bash
$ python3.9 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install chalice boto3 botocore 
(.venv) $ chalice new-project read_user_data
(.venv) $ cd read_user_data && pip freeze > requirements.txt
```

### Deployment

```bash
(.venv) $ chalice deploy --stage dev
```



## Testes via cURL
```
curl -d '{"x1":9}' <endereco informado no deploy>/predict_post -H 'content-type: application/json'
```