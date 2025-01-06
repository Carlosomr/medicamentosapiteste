from .database import db

class Medicamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(200))

    def __repr__(self):
        return f'<Medicamento {self.nome}>'
