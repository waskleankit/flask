import os
# import csv
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://root:@nkit2073@localhost:5432/postgres")
db = scoped_session(sessionmaker(bind=engine))




def main():
    # list of all flights
    flights = db.execute("SELECT * FROM flights").fetchall()
    for flight in flights:
        print(f"FLIGHT {flight.id}:{flight.origin} to {flight.destination}, {flight.duration} minutes")

    # prompt user to choose a flight.
    flight_id = int(input("\nFLIGHT_ID:"))
    flight = db.execute("SELECT origin, destination, duration FROM flights WHERE id =:id",
                        {"id": flight_id}).fetchone()

    # Make sure flight is valid.
    if flight is None:
        print("ERROR: No such flight")
        return

    # list passengers
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
                            {"flight_id": flight_id}).fetchall()
    print("\n Passengers:")
    for passenger in passengers:
        print(passenger.name)
    if len(passengers) == 0:
        print("No passengers")


if __name__ == "__main__":
    main()
