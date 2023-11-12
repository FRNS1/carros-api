from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    senha = db.Column(db.String, nullable=False)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Carros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    marca = db.Column(db.String, nullable=False)
    modelo = db.Column(db.String, nullable=False)
    foto = db.Column(db.String, nullable=False)
    km = db.Column(db.Float, nullable=True)
    ano = db.Column(db.Integer, nullable=True)
    motor = db.Column(db.String, nullable=True)
    cambio = db.Column(db.String, nullable=True)
    preco = db.Column(db.Float, nullable=True)
    dono_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    def __init__(self, nome, marca, modelo, foto, km, ano, motor, cambio, preco, dono_id):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.foto = foto
        self.km = km
        self.ano = ano
        self.motor = motor
        self.cambio = cambio
        self.preco = preco
        self.dono_id = dono_id