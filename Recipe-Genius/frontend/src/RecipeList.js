import React from 'react';

// RecipeList is a component that displays a list of recommended recipes
// Recipes is a prop that contains the recipe data to be shown
const RecipeList = ({ recipes }) => {
  return (
    <div>
      <h2>Recommended Recipes</h2>
      <ul>
        {recipes.map((recipe, index) => (
          <li key={index}>
            <h3>{recipe.name}</h3>
            <p>Ingredients: {recipe.ingredients.join(', ')}</p>
            <p>Calories: {recipe.calories}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default RecipeList;
