$(document).ready(function(){

    let i = 0;
    let y = 0;
    let z = 1;
    const ingredientsDic = [];
    const stepDic = [];
    const recipeName = document.getElementById("name");
    const user = document.getElementById("user");


    $('#addIngredient').click(() => {
            const ingredients = document.getElementById("ingredients");
            const ingredientLabel = document.createElement("Label");
            const newIngredient = document.createElement("INPUT");
            const amountLabel = document.createElement("Label");
            const amount = document.createElement("INPUT");
            const ingredientKey = "ingredient" + i;
            const ingredientValue = "amount" + i;


            ingredientLabel.setAttribute("for", ingredientKey);
            ingredientLabel.innerHTML = "Name: "
            newIngredient.setAttribute("type", "text");
            newIngredient.name = ingredientKey;
            amountLabel.setAttribute("for", ingredientValue);
            amountLabel.innerHTML = "Amount: ";
            amount.setAttribute("type", "text");
            amount.name = ingredientValue;
            $(amountLabel).addClass("mr-1")
            $(ingredientLabel).addClass("mr-1")
            $(amount).addClass("mb-3 mr-2")
        

            ingredients.appendChild(amountLabel);
            ingredients.appendChild(amount);
            ingredients.appendChild(ingredientLabel);
            ingredients.appendChild(newIngredient);
            ingredients.appendChild(document.createElement("BR"));
            ingredientsDic.push({key: ingredientKey, value: ingredientValue});
            console.log(ingredientsDic);
            i++;
        });
    
    $('#addStep').click(() => {
        const steps = document.getElementById("steps");
        const newStep = document.createElement("INPUT");
        const stepKeyValue = "step" + y;
        const stepNum = z + ".";
        const stepNumParagraph = document.createElement("P");

        newStep.setAttribute("type", "text");
        newStep.name = stepKeyValue;
        stepNumParagraph.innerHTML = stepNum;
        z++;
        y++;
        $(stepNumParagraph).addClass("d-inline mr-1")
        $(newStep).addClass("mb-3")

        stepDic.push({key: stepKeyValue, value: stepKeyValue})
        console.log(stepDic)
        steps.appendChild(stepNumParagraph);
        steps.appendChild(newStep);
        steps.appendChild(document.createElement("BR"))
    });

    $('#submit').click(() => {
        console.log("This is working!");
        $.ajax({
            url: "/add_recipe",
            type: "POST",
            data: { 'ingredients': JSON.stringify(ingredientsDic), 'steps': JSON.stringify(stepDic), 'name': JSON.stringify(recipeName), 'user': JSON.stringify(user), 'csrfmiddlewaretoken': '{{csrf_token}}' },

            success: function (json) {
                console.log(json);
                console.log("success");
            },
        });
    }
    )
    
});
