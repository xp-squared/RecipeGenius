import React, { useState } from 'react';

// IngredientInput is a componenet that allows users to enter ingredients as a comma seperated string
// useState manages the state of the input field
const IngredientInput = ({ onSubmit }) => {
  const [ingredients, setIngredients] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    // OnSubmit is a prop that handles form submission
    onSubmit(ingredients.split(',').map(ingredient => ingredient.trim()));
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Enter Ingredients (comma-separated):
        <input
          type="text"
          value={ingredients}
          onChange={(e) => setIngredients(e.target.value)}
        />
      </label>
      <button type="submit">Get Recipes</button>
    </form>
  );
};

export default IngredientInput;
