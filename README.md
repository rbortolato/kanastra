## Description
Projeto desenvolvido com Python3.9 e FastApi

Tudo que é necessário para rodar está no Docker

Criado um cache singleton para validação dos dados já enviados

Utilizado debugpy para debug.

Teste unitário utilizando PyTest

## Runing the project
### Docker
```
docker compose up -d
```

### Docker in Ubuntu
```
make dcup
```

### Python
```
pip install -r requirements.txt
python main.py
```

Will run in localhost:4080

### Manual Test with Swagger
```
access http://localhost:4080/docs
```

## Run tests
### Make
```
make tests
```
### Python
```
pytest
```
