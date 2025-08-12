from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import atexit
import json
import scraper  # your scraper.py module
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
app.config['SECRET_KEY'] = 'your-secret-key'
db = SQLAlchemy(app)


# Car model with VIN, image_url, and listing link added
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # e.g. 'available', 'sold'
    vin = db.Column(db.String(100), unique=True, nullable=True)  # VIN field
    image_url = db.Column(db.String(255), nullable=True)         # Image URL field
    link = db.Column(db.String(500), nullable=True)              # Listing link


#routes 
@app.route('/', methods=['GET', 'POST'])
def home():
    search = request.args.get('search')
    if search:
        cars = Car.query.filter(
            (Car.make.ilike(f'%{search}%')) | 
            (Car.model.ilike(f'%{search}%')) |
            (Car.status.ilike(f'%{search}%'))
        ).all()
    else:
        cars = Car.query.all()
    return render_template('home.html', cars=cars, search=search)







#main code
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
