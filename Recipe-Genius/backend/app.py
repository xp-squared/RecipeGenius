from flask import Flask, request, jsonify
from flask_cors import CORS
from model import recommender
import tensorflow as tf  # Import TensorFlow (we'll use it later)
import json

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes

# dummy data for example, placeholder for when we get a real database
recipes_db = [
    {"name": "Pasta", "ingredients": ["pasta", "tomato", "basil"], "calories": 400},
    {"name": "Salad", "ingredients": ["lettuce", "tomato", "cucumber"], "calories": 200},
    {"name": "Soup", "ingredients": ["water", "salt", "carrot"], "calories": 150},
    {"name": "Pizza", "ingredients": ["cheese", "tomato", "pepperoni"], "calories": 350},
    # add more recipes 
]

@app.route('/')
def home():
    return "Hello, Flask! Zane is here!" # check if server is running

# outputting probabilities
'''
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    ingredients = data.get('ingredients', [])
    
    # Just return random predictions
    predictions = recommender.recommend(ingredients)
    
    return jsonify({'predictions': predictions.tolist()})
'''

# outputting index of most likely recipe
@app.route('/recommend', methods=['POST'])  # Takes JSON payload with list of ingredients and returns recipes that contain at least one ingredient
def recommend():
    data = request.json
    print(f"Received data: {data}")  # Debugging statement
    ingredients = data.get('ingredients', [])
    print(f"Ingredients: {ingredients}")  # Debugging statement

    # Get indices of top 3 predictions
    top_indices = recommender.recommend(ingredients)
    print(f"Top indices: {top_indices}")  # Debugging statement

    # Map indices to recipes
    recommended_recipes = [recipes_db[i] for i in top_indices]
    print(f"Recommended recipes: {recommended_recipes}")  # Debugging statement

    return jsonify({'recipes': recommended_recipes})

if __name__ == '__main__':
    app.run(debug=True)