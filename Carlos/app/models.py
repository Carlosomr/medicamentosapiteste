from .database import db

class Medicamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(200))

    def __repr__(self):
        return f'<Medicamento {self.nome}>'

class Usuarios(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(10), nullable=False, unique=True)
    nome_usuario = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(80),nullable=False)
    senha = db.Column(db.String(8), nullable=False)

    def __repr__(self):
        return f'<Usuarios {self.usuario}>'