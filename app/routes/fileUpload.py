from flask import Blueprint, jsonify, make_response, request
from app.authenticate import token_required
from app.fileUploadService import upload_files_to_s3

files_bp = Blueprint('files', __name__)

@files_bp.route('/uploadfile', methods=['POST'])
def upload_file():
    file = request.files['file']
    output = upload_files_to_s3(file)
    if "https://carros-projeto.s3.amazonaws.com/" in output:
        return make_response(
            jsonify(
                mensagem="Arquivo enviado com sucesso",
                dados=f'{output}'
            ), 200
        )
    else:
        return make_response(
            jsonify(
                mensagem=f'{output}'
            ), 400
        )