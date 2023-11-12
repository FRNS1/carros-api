from flask import Flask
from .models import db
from .routes.users import users_bp
from .routes.carros import carros_bp
from .routes.login import login_bp
from flask_cors import CORS
from flask_migrate import Migrate
from .routes.fileUpload import files_bp

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:34215547@carros-usados-db.cgjfydnkuq23.us-east-1.rds.amazonaws.com/carrosusados'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.run(host='172.31.47.123', port=5000)
    app.run(debug=True)
    db.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(carros_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(files_bp)

    return app