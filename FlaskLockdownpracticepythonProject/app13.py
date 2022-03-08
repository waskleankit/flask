from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:@nkit2073@localhost:5432/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
          flights = Flight.query.all()
          return render_template("index12.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
          """ Book a flight."""

          #Get form information
          name = request.form.get("name")
          try:
                    flight_id = int(request.form.get("flight_id"))
          except ValueError:
                    return render_template("error.html", message="Invalid flight number.")

          #Make sure te flight exist
          flight = Flight.query.get(flight_id)
          if flight is None:
                    return render_template("error.html", message="No such flights with that id.")

          #Add passenger.
          flight.add_passenger(name)
          return render_template("success.html")

@app.route("/flights")
def flights():
          """Lists details about  all flights"""
          flights = Flight.query.all()
          return render_template("flights.html", flights=flights)


@app.route("/flights/<int:flight_id>")
def flight(flight_id):

          """lists details about a single flights."""

          #make suure  flight exists.
          flight = Flight.query.get(flight_id)
          if flight is None:
                    return render_template("error.html", message = "No  such flight")

          #Get all passengers
          passenger = flight.passengers
          return render_template("flight.html", flight=flight, passenger= passenger)


if __name__ == "__main__":
          with app.app_context():
              main()

