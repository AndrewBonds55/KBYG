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

# Define route for sending message
@app.route('/message', methods=['POST'])
def send_message():
    message = request.json['message']
    procedure_name = message.split(':')[0].strip().lower()
    procedure = Procedure.query.filter_by(name=procedure_name).first()

    if procedure:
        response = f"Here is some information about {procedure.name}:\n{procedure.description}"
    else:
        response = "I'm sorry, I don't have information about that procedure."

    return jsonify({'response': response})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)