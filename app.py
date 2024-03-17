from pathlib import Path
from db import db
from flask import Flask, render_template
import csv
app = Flask(__name__)
#this will make flask use a 'sqlite database witht the filename provided
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///store.db"
#this will make flask store the database file inthe path provided
#use "." for the instance path
app.instance_path = Path(".").resolve()
#connects db object with the app object - line 5
db.init_app(app)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/customers")
def customers():
    with open('data/customers.csv', "r") as csvfile:
        reader = csv.DictReader(csvfile)
        # print(type(reader))
        customers = []
        for row in reader:
            # print(type(row)) 
            # print((row)) 
            customers.append(row)
        return render_template("customers.html", customers=customers)
           
@app.route("/products")
def products():
    with open('data/products.csv', "r") as csvfile:
        reader = csv.DictReader(csvfile)
        products = []
        for row in reader:
            products.append(row)
        return render_template('products.html',products=products)


if __name__ == "__main__":
    app.run(debug=True, port=8888)