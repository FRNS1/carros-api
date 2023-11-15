from flask import Blueprint, jsonify, make_response, request
from app.models import Carros
from app.schemas import CarrosSchema, RegisterCarroSchema
from app import db
from app.authenticate import token_required

carros_bp = Blueprint('carros', __name__)

@carros_bp.route('/getcarros', methods=['GET'])
def get_carros():
    carros = Carros.query.all()
    carros_schema = CarrosSchema(many=True)
    carros_series = carros_schema.dump(carros)
    return make_response(
        jsonify(
            mensagem='Lista de carros',
            dados=carros_series
        ),
        200
    )

@carros_bp.route('/registercarro', methods=['POST'])
@token_required
def register_carro():
    data = request.get_json()
    if data:
        register_carro_schema=RegisterCarroSchema()
        erros = register_carro_schema.validate(data)
        if erros:
            return make_response(jsonify(erros), 400)
        novo_carro = Carros(data['nome'], data['marca'], data['modelo'], data['foto'], data['km'], data['ano'], data['motor'], data['cambio'], data['preco'], data['dono_id'])

        db.session.add(novo_carro)
        db.session.commit()

        return make_response(
            jsonify(
                mensagem='Carro criado com sucesso',
                dados=register_carro_schema.dump(novo_carro)
            ),
            201
        )
    return make_response(jsonify({"mensagem": "Nenhum dado recebido"}), 400)

@carros_bp.route('/updatecarro/<id>', methods=['PUT'])
@token_required
def update_carro(id):
    data = request.get_json()
    if data:
        carro = Carros.query.filter(Carros.id == id).first()
        carro.nome = data['nome']
        carro.marca = data['marca']
        carro.modelo = data['modelo']
        carro.ano = data['ano']
        carro.km = data['km']
        carro.motor = data['motor']
        carro.cambio = data['cambio']
        carro.preco = data['preco']
        carro.foto = data['foto']
        db.session.commit()

        return make_response(
            jsonify(
                mensagem='Carro atualizado com sucesso',
                dados=f'{carro}'
            ),
            201
        )
    return make_response(jsonify({"mensagem": "Nenhum dado recebido"}), 400)

@carros_bp.route('/deletecarro/<id>', methods=['DELETE'])
@token_required
def delete_carro(id):
    carro = Carros.query.filter(Carros.id == id).first()
    if not carro:
        return make_response(
            jsonify(
                mensagem='Carro não encontrado'
            ), 404
        )
    if carro:
        try:
            db.session.delete(carro)
            db.session.commit()
            return make_response(
                jsonify(mensagem='Carro deletado com sucesso.'),
                200
            )
        except Exception as e:
            return make_response(
                jsonify(
                    erro=f'{e}',
                    mensagem='Não foi possível deletar este carro.'
                ),
                500
            )

@carros_bp.route('/getcarro/<id>', methods=['GET'])
def get_carro(id):
    carro = Carros.query.filter(Carros.id == id).first()
    carros_schema = CarrosSchema()
    carro_encontrado = carros_schema.dump(carro)
    return make_response(
        jsonify(
            mensagem="Carro encontrado",
            dados=carro_encontrado
        )
    )
