# Restaurant Review Application

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
-  [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Description

The Restaurant Review Application is a Python-based project that allows users to manage and review restaurants and their customer reviews. It uses SQLAlchemy as the database ORM (Object-Relational Mapping) and MySQL as the database backend. The application provides features for creating, reading, updating, and deleting restaurants, customers, and reviews, as well as various query and aggregation methods.

## Features

- Create, update, and delete restaurants.
- Create, update, and delete customers.
- Add, edit, and delete reviews for restaurants.
- Query and aggregate data, including finding the highest-rated restaurant and customer reviews.
- Establish relationships between restaurants, customers, and reviews.
- Database migrations for maintaining database schema.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- `pip` package manager installed.
- MySQL server installed and running.

### Installation

1. Clone the repository:
   ```git clone https://github.com/yourusername/restaurant-review-app.git```

   2. Navigate to the project directory:
    ```
      cd restaurant-review-app
    
    ```
3. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   
   ```
4. Install project dependencies:
```
pip install -r requirements.txt
```
5. Seed the database with sample data:
```
python seeds.py

```
## Usage

Open a web browser and navigate to http://localhost:5000 to interact with the application.

Use the provided methods to manage restaurants, customers, reviews, and perform queries.

Project Structure
The project structure is organized as follows:

models.py: Defines SQLAlchemy models for restaurants, customers, and reviews.
seeds.py: Seeds the database with sample data.
app.py: Main application script for running the project.
README.md: This documentation file.
requirements.txt: Lists project dependencies.
Contributing
Contributions to this project are welcome. To contribute, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix: git checkout -b feature/your-feature-name.
Make your changes and commit them with clear and concise messages.
Push your changes to your forked repository.
Submit a pull request to the original repository.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
