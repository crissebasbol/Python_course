from flask import Flask

app = Flask(__name__)

# Decirle al servidor en qué URL vamos a ejecutar esta función
@app.route("/")
def hello_world():
    return "Hi world"


if __name__ == "__main__":
    app.run()
