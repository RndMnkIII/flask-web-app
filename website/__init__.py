from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'JLZXKJVOASIDFL.KSDFFPOASIDFDFW3E4TR089U'

    from .views import views
    from .auth import auth

    #Register blueprints with the Flask app
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app


