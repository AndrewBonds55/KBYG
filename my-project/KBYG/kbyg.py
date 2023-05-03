from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

#connect to the database
conn = sqlite3.connect('dental_database.db')
c = conn.cursor()

# Define a function to query the database for dental offices in a zip code
def get_dental_offices(zip_code):
    c.execute("SELECT * FROM dental_offices WHERE zip_code=?", (zip_code,))
    return c.fetchall()

# Define a function to query the database for prices for a particular procedure at a dental office
def get_procedure_price(dental_office_id, procedure_type):
    c.execute("SELECT price FROM dental_procedures WHERE dental_office_id=? AND procedure_type=?", (dental_office_id, procedure_type))
    return c.fetchone()

# Define a route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Define a route for the search results page
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        zip_code = request.form['zip_code']
        dental_offices = get_dental_offices(zip_code)
        results = []
        for dental_office in dental_offices:
            office_id = dental_office[0]
            office_name = dental_office[1]
            office_address = dental_office[2]
            office_city = dental_office[3]
            office_state = dental_office[4]
            office_zip = dental_office[5]
            prices = {}
            for procedure_type in ['cleaning', 'filling', 'crown']:
                price = get_procedure_price(office_id, procedure_type)
                if price:
                    prices[procedure_type] = price[0]
                else:
                    prices[procedure_type] = 'N/A'
            results.append((office_name, office_address, office_city, office_state, office_zip, prices))
        return render_template('results.html', results=results)
    else:
        return render_template('search.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
