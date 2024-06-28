import React, { useState } from 'react';
import IngredientInput from './IngredientInput';
import RecipeList from './RecipeList';

const App = () => {
  const [recipes, setRecipes] = useState([]);

  // this handles the interaction with the backend to fetch recommended recipes based on users entered ingredients
  const fetchRecipes = (ingredients) => {
    fetch('http://127.0.0.1:5000/recommend', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ ingredients }),
    })
      .then((response) => response.json())
      .then((data) => setRecipes(data.recipes))
      .catch((error) => console.error('Error:', error));
  };

  return (
    <div>
      <h1>Recipe Recommendation System</h1>
      <IngredientInput onSubmit={fetchRecipes} />
      <RecipeList recipes={recipes} />
    </div>
  );
};

export default App;
