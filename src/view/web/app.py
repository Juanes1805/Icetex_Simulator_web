import sys 
sys.path.append("src")
from flask import Flask
from view.web.routes import web_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'icetex_secret_key'  # Cambia esto en producción
    app.register_blueprint(web_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)