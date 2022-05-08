# O que fizemos: 

## Criacao do ambiente 

_Nota: digitar apenas a parte dos comandos **depois** do sinal de cifrão_

```bash
$ python3.8 -m venv .venv_ex
$ source .venv_ex/bin/activate
(.venv_ex) $ pip install chalice boto3 botocore
(.venv_ex) $ chalice new-project primeiro_projeto
```

Para rodar **localmente**

```bash
(.venv_ex) $ chalice local --stage {stage}
```

Para publicar na aws

```bash
(.venv_ex) $ chalice deploy --stage {stage}
```