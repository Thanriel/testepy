from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Olá, Azure App Service com Python, teste!"

if __name__ == "__main__":
    app.run()
