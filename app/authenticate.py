from flask import request, jsonify
from config import SECRET_KEY
import jwt
from app.models import Users
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify(mensagem='Você não enviou um token de autorização'), 401
        try:
            print('teste 2')
            data = jwt.decode(token.replace("b'", "").replace("'", ""), SECRET_KEY, algorithms=['HS256'])
            print(data)
            current_user = "teste"
        except Exception as e:
            return jsonify(mensagem='Token inválido ou expirado', erro=f'{e}'), 401
        return f(*args, **kwargs)
    return decorated