from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DentalOffice(db.Model):
    __tablename__ = 'dental_offices'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zip_code = db.Column(db.String(10), nullable=False)
    costs = db.relationship('Cost', backref='dental_office', lazy=True)

class Procedure(db.Model):
    __tablename__ = 'procedures'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    costs = db.relationship('Cost', backref='procedure', lazy=True)

class Cost(db.Model):
    __tablename__ = 'costs'
    id = db.Column(db.Integer, primary_key=True)
    dental_office_id = db.Column(db.Integer, db.ForeignKey('dental_offices.id'), nullable=False)
    procedure_id = db.Column(db.Integer, db.ForeignKey('procedures.id'), nullable=False)
    cost = db.Column(db.Float, nullable=False)

#In this schema, we have three tables: `dental_offices`, `procedures`, and `costs`. The `DentalOffice` table includes columns for the name, address, city, state, and zip code of each dental office. The `Procedure` table includes a column for the name of each procedure. The `Cost` table includes a column for the cost of each procedure at each dental office.