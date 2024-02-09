from sqlalchemy import create_engine, Column, Integer, String, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Define the PostgreSQL URL
DATABASE_URL = "postgresql://nodejs:nodejs@localhost:5432/test-db"

# Create a connection and a session
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def save_message(message: str):
    """Save a message to the database."""
    session = SessionLocal()
    todo = Todo(
        message=message,
        time=datetime.now()
    )
    session.add(todo)
    session.commit()
    session.close()

# Define the Todo table
class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, index=True)
    time = Column(DateTime)

# Create the table in the database
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    save_message("Hello, world!")


