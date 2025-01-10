from flask import current_app as app
from flask import jsonify, request, render_template, session
from .models import Medicamento, Usuarios
from .database import db
import bcrypt

@app.route('/administrador', methods=['GET'])
def administrador():
    return render_template('administrador.html')

@app.route('/medicamentos')
def cadastro():
    return render_template('cadastro.html')

@app.route('/lista', methods=['GET'])
def lista():
    return render_template('listamed.html')

@app.route('/', methods=['GET'])
def get_login():
    login = Usuarios.query.all()
    return jsonify([
    {   "id_usuario": user.id_usuario, 
        "usuario": user.usuario, 
        "nome_usuario": user.nome_usuario, 
        "email": user.email,
        "senha": user.senha  
    } for user in login]) 

@app.route('/cadastro', methods=['POST'])
def add_usuarios():
    data = request.get_json()
    
    # Verifica se o usuário já existe
    usuario_existente = Usuarios.query.filter_by(usuario=data['usuario']).first()
    if usuario_existente:
        return jsonify({"error": "Usuário já existe"}), 400

    # Extraia a senha do JSON enviado na solicitação
    senha = data.get('senha')
    
    if not senha:
        return jsonify({"error": "Senha é obrigatória"}), 400
    
    # Gerar o hash da senha
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    senha_hash_str = senha_hash.decode('utf-8')  # Converte o hash para string

    add_user = Usuarios(
        usuario=data['usuario'],
        nome_usuario=data['nome_usuario'],
        email=data['email'],
        senha=senha_hash_str  # Armazena o hash da senha como string
    )
    db.session.add(add_user)
    db.session.commit()
    return jsonify ({
        "id_usuario": add_user.id_usuario, 
        "usuario": add_user.usuario, 
        "nome_usuario": add_user.nome_usuario, 
        "email": add_user.email,
        "senha": add_user.senha }), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    senha = data.get('senha')

    user = Usuarios.query.filter_by(usuario=usuario).first()

    if user and bcrypt.checkpw(senha.encode('utf-8'), user.senha.encode('utf-8')):
        session['user_id'] = user.id_usuario  # Armazena o ID do usuário na sessão
        return jsonify({"message": "Login bem-sucedido!"}), 200
    else:
        return jsonify({"message": "Usuário ou senha inválidos!"}), 401

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
