from flask import Blueprint, jsonify, make_response, request
from werkzeug.security import generate_password_hash
from app.models import Users
from app import db
from app.schemas import register_user_schema
from app.authenticate import token_required

users_bp = Blueprint('users', __name__)

@users_bp.route('/getusers', methods=['GET'])
@token_required
def get_users():
    users = Users.query.all()
    return make_response(
        jsonify(
            mensagem='Lista de usuários',
            dados=users
        )
    )

@users_bp.route('/registeruser', methods=['POST'])
def register_user():
    data = request.get_json()
    if data:
        nome = data['nome']
        email = data['email']
        senha = data['senha']
        hash_senha = generate_password_hash(senha)
        user = Users(nome, email, hash_senha)
        db.session.add(user)
        db.session.commit()
        result = register_user_schema.dump(user)
        return make_response(
            jsonify(
                mensagem="Usuario criado com sucesso",
                dados=result
            ), 201
        )
    return make_response(
        jsonify(
            mensagem="Nenhum dado recebido"
        ), 400
    )