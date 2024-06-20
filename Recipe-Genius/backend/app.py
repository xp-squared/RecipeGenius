from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask! Zane is here!" # check if server is running

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json

    # extracts ingriedients from the request and returns an empty list of recipes
    # will modify later
    ingredients = data.get('ingredients') 

    # Placeholder for recommendation logic
    return jsonify({'recipes': []})

if __name__ == '__main__':
    app.run(debug=True)
