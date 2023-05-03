from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize Flask app
app = Flask(__name__)

# Set up database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dental_procedures.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

# Define dental procedures table
class Procedure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))

    def __init__(self, name, description):
        self.name = name
        self.description = description

# Define Marshmallow schema
class ProcedureSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description')

# Initialize Marshmallow schema
procedure_schema = ProcedureSchema()
procedures_schema = ProcedureSchema(many=True)

# Define route for adding a procedure
@app.route('/procedure', methods=['POST'])
def add_procedure():
    name = request.json['name']
    description = request.json['description']

    procedure = Procedure(name, description)

    db.session.add(procedure)
    db.session.commit()

    return procedure_schema.jsonify(procedure)

# Define route for getting all procedures
@app.route('/procedures', methods=['GET'])
def get_procedures():
    procedures = Procedure.query.all()

    return procedures_schema.jsonify(procedures)

# Define route for getting a single procedure
@app.route('/procedure/<id>', methods=['GET'])
def get_procedure(id):
    procedure = Procedure.query.get(id)

    return procedure_schema.jsonify(procedure)

# Define route for updating a procedure
@app.route('/procedure/<id>', methods=['PUT'])
def update_procedure(id):
    procedure = Procedure.query.get(id)

    name = request.json['name']
    description = request.json['description']

    procedure.name = name
    procedure.description = description

    db.session.commit()

    return procedure_schema.jsonify(procedure)

# Define route for deleting a procedure
@app.route('/procedure/<id>', methods=['DELETE'])
def delete_procedure(id):
    procedure = Procedure.query.get(id)

    db.session.delete(procedure)
    db.session.commit()

    return procedure_schema.jsonify(procedure)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
