from flask import Flask, render_template, request
from pymongo import MongoClient
from datetime import datetime
from flask import url_for

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['carshop']  # Replace 'yourdatabase' with your actual database name
collection = db['usernames']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_name', methods=['POST'])
def save_name():
    user_name = request.form['username']

  # Save the user's name in the database
    user_data = {'name': user_name}
    collection.insert_one(user_data)

    return render_template('result.html', username=user_name)

@app.route('/calculate', methods=['POST'])
def calculate():
    car_select = request.form['car']
    payment_term = int(request.form['paymentTerm'])

    car_price = get_car_price(car_select)
    total_payment = car_price / payment_term
    monthly_payment = total_payment / 12

    # Insert calculated data into MongoDB (you can customize this based on your needs)
    collection_name = 'calculations_' + datetime.now().strftime('%Y%m%d_%H%M%S')

    db[collection_name].insert_one({
        
        'timestamp': datetime.now(),
        'car_name': get_car_name(car_select),
        'car_price': car_price,
        'payment_term': payment_term,
        'total_payment': total_payment,
        'monthly_payment': monthly_payment,
        'car_image': car_select + '.jpg'
        })  
        
    
    return render_template(
        'result.html',
        car_name=get_car_name(car_select),
        car_price=car_price,
        payment_term=payment_term,
        total_payment=total_payment,
        monthly_payment=monthly_payment,
        car_image=car_select + '.jpg'
    )

@app.route('/view_data')
def view_data():
    # Fetch data from MongoDB
    collection_name = 'calculations_' + datetime.now().strftime('%Y%m%d')
    data = list(db[collection_name].find())

    return render_template('view_data.html', data=data)

@app.route('/history')
def history():
    # Fetch data from MongoDB using the latest username
    collection_name = 'calculations_20240117_134625'
    data = list(db[collection_name].find())

    return render_template('history.html', data=data)

def get_car_price(car_id):
    # In a real application, you would fetch this information from a database.
    # This is just a placeholder function.
    car_prices = {
        'car1': 88000,
        'car2': 130000,
        'car3': 144000,
        'car4': 175000,
        'car5': 212000,
    }

    return car_prices.get(car_id, 0)

def get_car_name(car_id):
    # In a real application, you would fetch this information from a database.
    # This is just a placeholder function.
    car_names = {
        'car1': 'Proton X50',
        'car2': 'Honda HRV',
        'car3': 'Toyota CH-R',
        'car4': 'Mazda 3',
        'car5': 'Nissan Qashqai',
    }

    return car_names.get(car_id, 'Unknown')

if __name__ == '__main__':
    app.run(debug=True)