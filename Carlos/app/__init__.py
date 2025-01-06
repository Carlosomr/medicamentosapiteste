# importando o flask
from flask import Flask
from .database import db

# criando uma função, responsavel pela aplicação.
def create_app():
    app = Flask(__name__) #instancia da classe Flask
    app.config.from_object('config.Config') #carrega os comandos do arquivo config.py
    db.init_app(app)

    with app.app_context(): # Cria um contexto da aplicação com app.app_context().Dentro desse contexto, importa o módulo routes.Garante que todas as rotas definidas em routes.py sejam registradas na aplicação Flask.
        from . import routes
        db.create_all()

    return app
