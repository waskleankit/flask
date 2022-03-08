from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:@nkit2073@localhost:5432/postgres")
db = scoped_session(sessionmaker(bind=engine))

def main():
                flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
                for flight in flights:
                                print(f"{flight.origin} to {flight.destination}, {flight.duration} minute.")
if __name__ == "__main__":
                main()
