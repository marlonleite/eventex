# Eventex

Sistema de eventos encomendado pela morena.

[![Build Status](https://travis-ci.org/marlonleite/eventex.svg?branch=master)](https://travis-ci.org/marlonleite/eventex)

## Como Desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com python 3.5.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instancia com o .env.
6. Execute os testes.

```console
git clone git@github.com:marlonleite/eventex.git wttd
cd wttd
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env``
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instancia no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRETE_KEY segura para a instância
4. Defina o DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

````console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_kEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuração de email
git push heroku mastes --force
```