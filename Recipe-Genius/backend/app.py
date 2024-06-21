from flask import Flask, request, jsonify
import tensorflow as tf  # Import TensorFlow (we'll use it later)
import json

app = Flask(__name__)

# dummy data for example, placeholder for when we get a real database
recipes_db = [
    {"name": "Pasta", "ingredients": ["pasta", "tomato", "basil"], "calories": 400},
    {"name": "Salad", "ingredients": ["lettuce", "tomato", "cucumber"], "calories": 200},
    # add more recipes 
]

@app.route('/')
def home():
    return "Hello, Flask! Zane is here!" # check if server is running

@app.route('/recommend', methods=['POST']) # takes json payload with list of ingredients and returns recipes that contain at least one ingredient
def recommend():
    data = request.json
    ingredients = data.get('ingredients', [])
    
    # return recipes that have at least one matching ingredient
    recommended_recipes = [
        recipe for recipe in recipes_db if any(ingredient in recipe['ingredients'] for ingredient in ingredients)
    ]
    
    return jsonify({'recipes': recommended_recipes})

if __name__ == '__main__':
    app.run(debug=True)
