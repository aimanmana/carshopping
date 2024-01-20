# carshopping
A website that the user can know more installment payment for each type of cars
**BACKGROUND**

The car catalog website comes from the changing landscape of digital automotive platforms. This project is set within the context in which consumers need not just accurate and extensive information about a wide choice of cars, but also an intuitive interface that allows buyers and sellers to connect. 

**OBJECTIVES**

The main objective of the car catalog website is to provide consumers with comprehensive and accurate information about a wide range of vehicles.. Pricing information is presented in a transparent manner. The car catalog website's design highlights user experience by creating a straightforward and easy-to-use interface. Navigation is maintained simple and basic, with well-defined categories for quick browsing and information access. It also serves as a platform for facilitating relationships between potential buyers and sellers, which is accomplished through seamless interaction with dealerships. This guarantees that users can make solid decisions based on an in depth understanding of each vehicle's characteristics and pricing.

**PRODUCT PERSPECTIVE**

From a product point of view, it functions as a repository of accurate and precise data about a wide range of cars, including specifications, features, and pricing. This digital hub is designed to fulfill the demands of both car enthusiasts seeking detailed technical information and potential customers exploring the market for their next vehicle. The website provides a database, explaining each vehicle within the wider car ecosystem. It also provides a thorough explanation of pricing structures. Besides being an informative resource, the car catalog website is also a facilitator of relationships in the automotive sector. By easily connecting with dealerships and sellers, the platform becomes a virtual marketplace.

**GENERAL CONSTRAINTS**

The dashboard for our web-based application is being developed with several general constraints that will greatly affect the project. Financial restrictions, which include limitations on financial resources allocated throughout the development lifecycle, are an important consideration. This comprises costs for early design, following development, extensive testing, and continuing maintenance. Another important factor is resource limits, specifically the availability of qualified personnel and the necessary tools for the project. Securing a skilled team of designers and developers is critical to ensuring the dashboard's successful implementation. Data privacy concerns are another important aspect of our development efforts. Cooperation with data protection laws and regulations is critical for protecting user privacy and ensuring the proper management of personal or sensitive information.

**SYSTEM ARCHITECTURE**



The web application, created with the Flask framework for Python, integrates numerous components to provide a solid and user-friendly experience. Flask routes manage the front-end, including various user interactions and form submissions. MongoDB serves as the backend database, conveniently storing user and calculation data in separate collections. HTML templates improve the user experience by allowing for flexible data display and form-based interaction. User interaction involves navigating various paths, submitting forms, and doing data calculations. The PyMongo library is used to establish a connection to MongoDB. Security considerations include strong validation and cleaning of user input, which may be strengthened by user authentication and authorization. Scalability is addressed through regular evaluation and optimization for increasing user and calculation demands. The application and MongoDB server are hosted with security settings and environment variables configured during deployment. Logging and monitoring, which are critical for error detection and performance evaluation, are implemented to ensure the application's dependability and efficiency.

**CLOUD PLATFORM**

MongoDB will be used by the website to store the data. MongoDB Compass is a graphical user interface tool designed to simplify interaction with MongoDB databases. Offering a user-friendly interface, it facilitates local and remote connections to MongoDB servers. The tool enables users to visually explore data within collections, build queries with a visual query builder, manage indexes, visualize schemas, analyze query performance, and construct complex aggregation pipelines. Compass also provides features for real-time server monitoring, document validation, and overall database management, making it a comprehensive tool for developers, database administrators, and users seeking a visual and intuitive way to work with MongoDB.



**HOMEPAGE :** 

We are using ‘Flask’ to create our homepage. Flask is a lightweight web framework for Python, known for its simplicity and flexibility. Flask provides the essential tools for web development without imposing a rigid structure. Its routing system enables easy URL mapping to Python functions, and the integration of the Jinja2 template engine allows dynamic HTML generation. This homepage will display the type of a car, the payment term and also the history payment.



**INSTALLATION**

STEP 1 : SET UP DATABASE

- Install MongoDB Compass:
- If you haven't already, download and install MongoDB Compass from the official MongoDB website: MongoDB Compass Download.

- Open MongoDB Compass:
- Once installed, open MongoDB Compass.

- Connect to MongoDB Server:
- Click on the "Connect" button to connect to your MongoDB server. 
- If you're running MongoDB locally, Compass may automatically connect to the default localhost:27017. 
- If your MongoDB server is running on a different host or port, you can customize the connection settings.

- Create a Database:
- After connecting, click on the "Create Database" button.
- Enter the name for your new database in the dialog box that appears. 
- Choose a name for your database and click the "Create Database" button.

- Verify the Database:
- After creating the database, you will see it listed in the left sidebar of MongoDB Compass under the "Databases" section. 

STEP 2 : SET UP WEBSITE

- Install Flask:
- pip install Flask (Run In Terminal)

- Create a file named ‘app.py’
- Insert this code into ‘app.py’

from flask import Flask, render_template, request
app = Flask(__name__)
 @app.route('/')
def index():
    return render_template('index.html')
@app.route('/calculate', methods=['POST'])
def calculate():
    car_select = request.form['car']
    payment_term = int(request.form['paymentTerm'])
    car_price = get_car_price(car_select)
    installment = car_price / payment_term
    return render_template(
        'result.html',
        car_name=get_car_name(car_select),
        car_price=car_price,
        payment_term=payment_term,
        installment=installment,
        car_image=car_select + '.jpg'
    )
 
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

- Create a folder named ‘templates’ and add two HTML files
- Insert this code into ‘index.html’ and this is for homepage set up

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    <title>Car Shopping</title>
</head>
<body>
    <div class="container">
        <h1>Car Shopping</h1>
        <form action="/calculate" method="post">
            <label for="car">Choose a Car:</label>
            <select id="car" name="car">
                <option value="car1">Car 1</option>
                <option value="car2">Car 2</option>
                <option value="car3">Car 3</option>
                <option value="car4">Car 4</option>
                <option value="car5">Car 5</option>
            </select>
 
            <label for="paymentTerm">Choose Payment Term:</label>
            <select id="paymentTerm" name="paymentTerm">
                <option value="8">8 years</option>
                <option value="10">10 years</option>
            </select>
 
            <button type="submit">Calculate Payment</button>
        </form>
    </div>
</body>
</html>
Insert this code into ‘result.html’ and this is for the set up of result page
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    <title>Car Shopping - Result</title>
</head>
<body>
    <div class="container">
        <h2>Car Details</h2>
        <p>Car: {{ car_name }}</p>
        <p>Total Price: ${{ car_price }}</p>
        <p>Installment Payment ({{ payment_term }} years): ${{ installment|round(2) }}</p>
        <img src="{{ url_for('static', filename='car_images/' + car_image) }}" alt="{{ car_name }}">
    </div>
</body>
</html>

- Create a folder named ‘static’ and add a file named ‘styles.css’
- This code is for page layout and font setting

body {
    font-family: Arial, sans-serif;
    background-color: #FFD700;
    margin: 0;
    padding: 0;
}
 
.container {
    max-width: 600px;
    margin: 50px auto;
    background-color: #fff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
 
form {
    margin-bottom: 20px;
}
 
button {
    background-color: #4caf50;
    color: #fff;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
 
button:hover {
    background-color: #45a049;
}

- Create a folder named ‘car_images’ and add images with filenames car1.jpg, car2.jpg and so on.
- Save this folder under the ‘static’ folder.

- Run the Flask application:
- python app.py (Run in terminal)
- Visit http://127.0.0.1:5000/ in your web browser to use the car shopping website.

- To divide the installment payment by 12 to represent monthly payments
- Modify the calculate function in ‘app.py’

@app.route('/calculate', methods=['POST'])
def calculate():
    car_select = request.form['car']
    payment_term = int(request.form['paymentTerm'])
    car_price = get_car_price(car_select)
    total_payment = car_price / payment_term
    monthly_payment = total_payment / 12
    return render_template(
        'result.html',
        car_name=get_car_name(car_select),
        car_price=car_price,
        payment_term=payment_term,
        total_payment=total_payment,
        monthly_payment=monthly_payment,
        car_image=car_select + '.jpg'
    )

- Update the ‘result.html’

</head>
<body>
    <div class="container">
        <h2>Car Details</h2>
        <p>Car: {{ car_name }}</p>
        <p>Total Price: ${{ car_price }}</p>
        <p>Installment Payment ({{ payment_term }} years): ${{ total_payment|round(2) }}</p>
        <p>Monthly Payment: ${{ monthly_payment|round(2) }}</p>
        <img src="{{ url_for('static', filename='car_images/' + car_image) }}" alt="{{ car_name }}">
    </div>

STEP 3 : CONNECT WEBSITE TO DATABASE

- To connect your Flask application to a MongoDB database, you can use a MongoDB driver like pymongo
- pip install pymongo (Run in terminal)

- Modify your Flask app

from flask import Flask, render_template, request
from pymongo import MongoClient
app = Flask(__name__)
# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['yourdatabase']  # Replace 'yourdatabase' with your actual database name
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/calculate', methods=['POST'])
def calculate():
    car_select = request.form['car']
    payment_term = int(request.form['paymentTerm'])
    car_price = get_car_price(car_select)
    total_payment = car_price / payment_term
    monthly_payment = total_payment / 12
 
    # Insert calculated data into MongoDB (you can customize this based on your needs)
    db.calculations.insert_one({
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
 
def get_car_price(car_id):
    # In a real application, you might fetch this information from the database.
    car_prices = {
        'car1': 88000,
        'car2': 130000,
        'car3': 144000,
        'car4': 175000,
        'car5': 212000,
    }
    return car_prices.get(car_id, 0)
def get_car_name(car_id):
    # In a real application, you might fetch this information from the database.
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

- Specify a Custom Collection:
- You could use the current date as part of the collection name to organize data by date.
- Insert this code into ‘app.py’

[from](url) datetime import datetime
collection_name = 'calculations_' + datetime.now().strftime('%Y%m%d')
db[collection_name].insert_one({
  # your data here
})
Store Additional Information:
Include additional information in the document that you insert.
 This could be user information, timestamps, or any other relevant details.
Insert this code into ‘app.py’
db.calculations.insert_one({
 'user_id': '12345',
 'timestamp': datetime.now(),
 'car_name': get_car_name(car_select),
 'car_price': car_price,
 'payment_term': payment_term,
  'total_payment': total_payment,
  'monthly_payment': monthly_payment,
   'car_image': car_select + '.jpg'
})
