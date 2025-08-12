from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
app.config['SECRET_KEY'] = 'your-secret-key'
db = SQLAlchemy(app)



@app.route("/")
def home():
    return "Railway deployment test successful!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
