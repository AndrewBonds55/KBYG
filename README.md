# KBYG

# Dental Procedure Database (Know Before You Go)

This Flask project is a tool for managing a database of dental procedure prices in different zip codes. It allows users to view and update prices for each procedure at individual dental offices.

## Technologies

This project is built using Python, Flask, and SQLAlchemy. It also uses a number of other libraries, including Flask-WTF for form handling, and Flask-Login for user authentication.

## Setup

To run this project locally, you'll need to set up a virtual environment and install the required dependencies. You can do this by running the following commands:

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

You'll also need to set up a PostgreSQL database and update the `config.py` file with your database credentials.

Once you've installed the dependencies and set up your database, you can run the project by running the following command:

```
flask run
```

## Project Structure

This project is organized into several modules:

- `kbyg.py`: the main Flask application (my-project>KBYG>kbyg.py)
- `models.py`: the SQLAlchemy models for the database
- `views.py`: the Flask views for rendering HTML templates
- `static/`: static files, including CSS and JavaScript
- `templates/`: HTML templates for rendering the user interface

## Domain Model

This project uses a domain model that consists of three entities:

- `ZipCode`: a zip code that corresponds to a specific geographic area
- `DentalOffice`: a dental office that provides dental procedures
- `Procedure`: a dental procedure that can be performed at a dental office

These entities are related as follows:

- Each `ZipCode` can have many `DentalOffices`
- Each `DentalOffice` can offer many `Procedures`
- Each `Procedure` can be performed at many `DentalOffices`

## Retrieving and Storing Data

This project uses Flask's built-in SQLAlchemy ORM to retrieve and store data in the PostgreSQL database. The `models.py` file defines the database schema and provides methods for querying the database.



## Contact

If you have any questions or feedback about this project, you can contact me at atbonds1@buffs.wtamu.edu
