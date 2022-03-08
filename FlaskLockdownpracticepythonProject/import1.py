import os
import csv

from flask import Flask, render_template,request
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:@nkit2073@localhost:5432/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
                f = open("F:\python\\flights.csv")
                reader = csv.reader(f)
                for o, des, dur in reader:
                          flight = Flight(origin=o, destination = des, duration = dur)
                          db.session.add(flight)
                          print(f"Added flight from {o} to {des} lasting {dur} minutes")

                db.session.commit()

if __name__ == "__main__":
          with app.app_context():
                    main()
