### 🛠️ Para rodar o projeto:

Na pasta do seu projeto você deve criar o venv. 

No terminal rode:
```
virtualenv venv --python=/usr/bin/python3.10
source venv/bin/activate
```
<li>Para rodar seu container no Docker com Django e Postgres
ainda no terminal:</li>

```
sudo docker-compose up  
```


<li>Ou apenas para testar localmente: </li>

```
python3 manage.py runserver
```

http://localhost:8000/api/v1/

Necessário criar o usuário, dentro da venv,
Exemplo:
```
python3 manage.py createsuperuser --email admin@fundsfinder.com --username admin
```
```
http://localhost:8000/api/v1/fundos
```
