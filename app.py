# run.py

from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "¡Hola, Flask está corriendo bien!"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
