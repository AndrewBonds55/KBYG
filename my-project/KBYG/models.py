from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DentalOffice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.String(10), nullable=False)
    procedures = db.relationship('DentalProcedure', backref='dental_office', lazy=True)

class DentalProcedure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dental_office_id = db.Column(db.Integer, db.ForeignKey('dental_office.id'), nullable=False)
    procedure_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
