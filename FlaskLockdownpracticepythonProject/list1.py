import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:@nkit2073@localhost:5432/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
                flights = Flight.query.all()
                for flight in flights:
                                print(f"{flight.origin} to {flight.destination}, {flight.duration} minute.")
if __name__ == "__main__":
          with app.app_context():
                    main()
