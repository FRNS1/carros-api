import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from config import SECRET_KEY
from flask import Blueprint, jsonify, make_response, request
from app.models import Users
import datetime

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data:
        email = data['email']
        senha = data['senha']
        print("teste")
        user = Users.query.filter(Users.email == email).first()
        if not user:
            return make_response(
                jsonify(
                    mensagem='Usuario nao encontrado'
                )
            )
        if user and check_password_hash(user.senha, senha):
            token = jwt.encode({'username': user.email, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)},
                                SECRET_KEY)
            return jsonify(mensagem='Validacao sucedida', token=f'{token.encode()}',
                           exp=datetime.datetime.now() + datetime.timedelta(hours=98),
                           user=f'{user.id}')

        return jsonify(mensagem='credenciais incorretas')

