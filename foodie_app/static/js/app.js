$(document).ready(function(){

    $('#addIngredient').click(() => {
            const ingredients = document.getElementById("ingredients");
            const ingredientLabel = document.createElement("Label");
            const newIngredient = document.createElement("INPUT");
            const amountLabel = document.createElement("Label");
            const amount = document.createElement("INPUT");

            ingredientLabel.setAttribute("for", newIngredient);
            ingredientLabel.innerHTML = "Name:"
            newIngredient.setAttribute("type", "text");
            newIngredient.name = "ingredient";
            amountLabel.setAttribute("for", amount);
            amountLabel.innerHTML = "Amount:";
            amount.setAttribute("type", "text");
            amount.name = "amount";

            ingredients.appendChild(amountLabel);
            ingredients.appendChild(amount);
            ingredients.appendChild(ingredientLabel);
            ingredients.appendChild(newIngredient);
        });
    
    $('#addStep').click(() => {
        const steps = document.getElementById("steps");
        const newStep = document.createElement("INPUT");

        newStep.setAttribute("type", "text");
        newStep.name = "step"

        steps.appendChild(newStep);
    });
});
// NEED TO ADD BREAKS AFTER NEW ELEMENTS