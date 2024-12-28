from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes.books import books_bp
    from .routes.members import members_bp

    app.register_blueprint(books_bp, url_prefix='/books')
    app.register_blueprint(members_bp, url_prefix='/members')

    return app
