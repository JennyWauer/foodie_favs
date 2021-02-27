$(document).ready(function(){

    let i = 0;
    let y = 0;
    let z = 1;
    // let ii = 0;
    // let yy = 0;
    // const ingredientsDic = [];
    // const stepDic = [];
    // const recipeName = document.getElementById("name");
    // const user = document.getElementById("user");


    $('#addIngredient').click(() => {
            const ingredients = document.getElementById("ingredients");
            const ingredient = "ingredient";
            const quantity = "quantity";
            const measurement = "measurement";
            const div = document.createElement("div");
            div.innerHTML = '<div>\n' +
                '<form action="/home/add_ingredient" method="POST" name="ingredientForm" class="ingredientForm">' +
                '<label for="quantity" class="mr-1">Amount: </label>' +
                '<input type="text" name="quantity" id="quantity" class="mr-1">' +
                '<select name="measurement" id="measurement" class="mr-1">' +
                '<option value="tsp">tsp.</option>' +
                '<option value="tbsp">tbsp.</option>' +
                '<option value="fl-oz">fl oz</option>' +
                '<option value="mL">mL</option>' +
                '<option value="cup">cup</option>' +
                '<option value="ounce">oz</option>' +
                '<option value="lb">lb</option>' +
                '<option value="g">g</option>' +
                '</select>' +
                '<label for="name" class="mr-1">Name: </label>' +
                '<input type="text" name="name" id="name" class="mr-1">' +
                '<input type="submit" value="save ingredient" class="submitIngredient rounded shadow-sm bg-white rounded">\n' +
                '</form>' +
                '</div>';

            ingredients.appendChild(div);
            i++;

            function getCookie(c_name) {
                if(document.cookie.length > 0) {
                    c_start = document.cookie.indexOf(c_name + "=");
                    if(c_start != -1) {
                        c_start = c_start + c_name.length + 1;
                        c_end = document.cookie.indexOf(";", c_start);
                        if(c_end == -1) c_end = document.cookie.length;
                        return unescape(document.cookie.substring(c_start,c_end));
                    }
                }
                return "";
            }

            $('.submitIngredient').click((e) => {
                e.preventDefault()
                const form = $('.ingredientForm')
                $.ajax({
                    url: form.attr('action'),
                    type: form.attr('method'),
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken'),
                      },
                    data: form.serialize(),
                })
                .done(function(response){
                    console.log(response);
                })
                return false;
            })
        });
    $('#addStep').click(() => {
        const steps = document.getElementById("steps");
        const newStep = document.createElement("div");
        const step = "step" + y;
        const stepNum = z;

        newStep.innerHTML = '<div>\n' +
            '<form action="/home/add_step" method="POST" class="stepForm">' +
            '<p class="mr-1 d-inline">' + stepNum + '.</p>' +
            '<input type="text" name="' + step + '" id="' + step + '" class="mb-1 mr-1">' +
            '<input type="submit" value="save step" class="submitStep rounded shadow-sm bg-white rounded">\n' +
            '<input type="hidden" name="stepNum" id="stepNum>'
            '</form>\n' +
            '</div>';
        
        y++;
        z++;
    });
    
    $('add-item').click(() => {
        console.log('hello')
        const list = document.getElementById("shopping-list");
        const itemLabel = document.createElement("Label")
        const listItem = document.createElement("INPUT")
    })
});
