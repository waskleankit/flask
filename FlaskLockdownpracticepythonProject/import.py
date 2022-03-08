import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

engine = create_engine("postgresql://postgres:@nkit2073@localhost:5432/postgres")
db = scoped_session(sessionmaker(bind=engine))


def main():
                f = open("F:\python\\flights.csv")
                reader = csv.reader(f)
                for o, des, dur in reader:
                                db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
                                           {"origin": o, "destination": des, "duration": dur})
                                print(f"Added flight from {o} to {des} lasting {dur} minutes")

                db.commit()

if __name__ == "__main__":
                main()
