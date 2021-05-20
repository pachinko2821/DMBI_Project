from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': utils.location_names()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = request.form['bhk']
    bath = request.form['bath']

    response = jsonify({
        'estimated_price':utils.get_estimated_price(total_sqft, location, bhk, bath)
    })
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

if __name__ == "__main__":
    print("[*] Starting flask server...")
    app.run()