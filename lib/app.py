from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Customer, Restaurant, Review

engine = create_engine('your_database_url_here')
Session = sessionmaker(bind=engine)
session = Session()

# Test your methods here