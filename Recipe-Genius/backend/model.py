import tensorflow as tf  
import numpy as np

# Dummy model
class RecipeRecommender:
    def __init__(self):
        # dummy model with random weights
        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(10, activation='relu'),
            tf.keras.layers.Dense(3, activation='softmax')
        ])
    
    def recommend(self, ingredients):
        # Dummy recommendation logic
        input_data = np.random.rand(1, len(ingredients))  # Random input for example
        predictions = self.model.predict(input_data)
        top_indices = np.argsort(predictions[0])[-3:]  # Get indices of top 3 predictions
        return top_indices

recommender = RecipeRecommender()