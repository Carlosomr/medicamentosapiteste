from flask import current_app as app
from flask import jsonify, request, render_template
from .models import Medicamento
from .database import db

@app.route('/')
def cadastro():
    return render_template('cadastro.html')

@app.route('/lista', methods=['GET'])
def lista():
    return render_template('listamed.html')

@app.route('/api/medicamentos', methods=['GET'])
def get_medicamentos():
    medicamentos = Medicamento.query.all()
    return jsonify([{"id": med.id, "nome": med.nome, "quantidade": med.quantidade, "descricao": med.descricao} for med in medicamentos])

@app.route('/api/medicamentos', methods=['POST'])
def add_medicamento():
    data = request.get_json()
    novo_medicamento = Medicamento(
        nome=data['nome'],
        quantidade=data['quantidade'],
        descricao=data.get('descricao', '')
    )
    db.session.add(novo_medicamento)
    db.session.commit()
    return jsonify({"id": novo_medicamento.id, "nome": novo_medicamento.nome, "quantidade": novo_medicamento.quantidade, "descricao": novo_medicamento.descricao}), 201

@app.route('/api/medicamentos/<int:id>', methods=['GET'])
def get_medicamento(id):
    medicamento = Medicamento.query.get_or_404(id)
    return jsonify({"id": medicamento.id, "nome": medicamento.nome, "quantidade": medicamento.quantidade, "descricao": medicamento.descricao})

@app.route('/api/medicamentos/<int:id>', methods=['PUT'])
def update_medicamento(id):
    data = request.get_json()
    medicamento = Medicamento.query.get_or_404(id)
    medicamento.nome = data.get('nome', medicamento.nome)
    medicamento.quantidade = data.get('quantidade', medicamento.quantidade)
    medicamento.descricao = data.get('descricao', medicamento.descricao)
    db.session.commit()
    return jsonify({"id": medicamento.id, "nome": medicamento.nome, "quantidade": medicamento.quantidade, "descricao": medicamento.descricao})

@app.route('/api/medicamentos/<int:id>', methods=['DELETE'])
def delete_medicamento(id):
    medicamento = Medicamento.query.get_or_404(id)
    db.session.delete(medicamento)
    db.session.commit()
    return jsonify({"message": "Medicamento removido com sucesso"}), 200

@app.route('/api/medicamentos/delete', methods=['DELETE'])
def delete_all_medicamentos():
    try:
        num_deleted = Medicamento.query.delete()
        db.session.commit()
        return jsonify({"message": f"Todos os {num_deleted} medicamentos foram removidos com sucesso"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Erro ao deletar medicamentos", "error": str(e)}), 500

