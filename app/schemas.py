from marshmallow import Schema, fields

class CarrosSchema(Schema):
    id = fields.Integer()
    nome = fields.String()
    marca = fields.String()
    modelo = fields.String()
    foto = fields.String()
    km = fields.Float()
    ano = fields.Integer()
    motor = fields.String()
    cambio = fields.String()
    preco = fields.Float()
    dono_id = fields.Integer()

class RegisterCarroSchema(Schema):
    id = fields.Integer(dump_only=True)
    nome = fields.String()
    marca = fields.String()
    modelo = fields.String()
    foto = fields.String()
    km = fields.Float()
    ano = fields.Integer()
    motor = fields.String()
    cambio = fields.String()
    preco = fields.Float()
    dono_id = fields.Integer()


class RegisterUserSchema(Schema):
    class Meta:
        fields = ('id', 'nome', 'email', 'senha')

register_user_schema = RegisterUserSchema()