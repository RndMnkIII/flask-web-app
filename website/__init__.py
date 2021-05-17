from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'JLZXKJVOASIDFL.KSDFFPOASIDFDFW3E4TR089U'

    return app


