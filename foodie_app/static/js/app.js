$(document).ready(function(){

    let i = 0;
    let y = 0;
    let z = 1;
    let ii = 0;
    let yy = 0;
    const ingredientsDic = [];
    const stepDic = [];
    const recipeName = document.getElementById("name");
    const user = document.getElementById("user");


    $('#addIngredient').click(() => {
            const ingredients = document.getElementById("ingredients");
            const ingredient = "ingredient" + i;
            const quantity = "quantity" + i;
            const measurement = "measurement" + i;
            const div = document.createElement("div");
            div.innerHTML = '<div>\n' +
                '<form action="/home/add_ingredient" method="POST" class=".ingredientForm">' +
                '<label for="' + quantity + '" class="mr-1">Amount: </label>' +
                '<input type="text" name="' + quantity + '" id="' + quantity + '" class="mr-1">' +
                '<select name="' + measurement + '" id="' + measurement + '" class="mr-1">' +
                '<option value="tsp">tsp.</option>' +
                '<option value="tbsp">tbsp.</option>' +
                '<option value="fl-oz">fl oz</option>' +
                '<option value="mL">mL</option>' +
                '<option value="cup">cup</option>' +
                '<option value="ounce">oz</option>' +
                '<option value="lb">lb</option>' +
                '<option value="g">g</option>' +
                '</select>' +
                '<label for="' + ingredient + '" class="mr-1">Name: </label>' +
                '<input type="text" name="' + ingredient + '" id="' + ingredient + '" class="mr-1">' +
                '<input type="submit" value="save ingredient" class="submitIngredient rounded shadow-sm bg-white rounded">\n' +
                '</form>' +
                '</div>';
            
            ingredients.appendChild(div);
            i++;
            // ingredientsDic.push({key: ingredientKey, value: ingredientValue});
            // console.log(ingredientsDic);
            // i++;
        });
    
    $('.submitIngredient').click(() => {
        $.ajax({
            url: '/home/add_ingredient',
            method: 'POST',
            data: $('.ingredientForm').serialize()
        })
        .done(function(response){
            console.log(response);
        })
        return false;
    })

    $('#addStep').click(() => {
        const steps = document.getElementById("steps");
        const newStep = document.createElement("div");
        const step = "step" + y;
        const stepNum = z;

        newStep.innerHTML = '<div>\n' +
            '<form action="/home/add_step" method="POST">' +
            '<p class="mr-1 d-inline">' + stepNum + '.</p>' +
            '<input type="text" name="' + step + '" id="' + step + '" class="mb-1 mr-1">' +
            '<input type="submit" value="save step" class="submitStep rounded shadow-sm bg-white rounded">\n' +
            '</form>\n' +
            '</div>';
        
        y++;
        z++;
        steps.appendChild(newStep);
        // stepDic.push({key: stepKeyValue, value: stepKeyValue})
        // console.log(stepDic)
    });

    // $('#submit').click(() => {
    //     console.log("This is working!");
    //     $.ajax({
    //         url: "/add_recipe",
    //         type: "POST",
    //         data: { 'ingredients': JSON.stringify(ingredientsDic), 'steps': JSON.stringify(stepDic), 'name': JSON.stringify(recipeName), 'user': JSON.stringify(user), 'csrfmiddlewaretoken': '{{csrf_token}}' },

    //         success: function (json) {
    //             console.log(json);
    //             console.log("success");
    //         },
    //     });
    // }
    // )
    
    $('add-item').click(() => {
        console.log('hello')
        const list = document.getElementById("shopping-list");
        const itemLabel = document.createElement("Label")
        const listItem = document.createElement("INPUT")
    })
});
