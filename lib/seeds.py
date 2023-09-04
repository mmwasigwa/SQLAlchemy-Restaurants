from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

engine = create_engine('your_database_url_here')
Session = sessionmaker(bind=engine)
session = Session()

# Create sample data
restaurant1 = Restaurant(name='Restaurant A', price=3)
restaurant2 = Restaurant(name='Restaurant B', price=2)

customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Smith')

# Add data to the session and commit
session.add_all([restaurant1, restaurant2, customer1, customer2])
session.commit()
