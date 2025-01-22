from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    # Configurações
    app.config.from_object('config')
    app.config.from_pyfile('config.py', silent=True)
    
    # Inicializar extensões
    db.init_app(app)
    
    # Registrar Blueprints
    from app.routes import main_routes
    app.register_blueprint(main_routes)
    
    return app
