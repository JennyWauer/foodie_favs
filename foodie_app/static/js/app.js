$(document).ready(function(){

  let z = 1;

  mybutton = document.getElementById("topBtn");

  window.onscroll = function() {scrollFunction()};
  
  function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      mybutton.style.display = "block";
    } else {
      mybutton.style.display = "none";
    }
  }
  
  $('#topBtn').click(
      function scrollToTop() {
          document.body.scrollTop = 0; 
          document.documentElement.scrollTop = 0;
        }
  )

  $('#addItem').click(
    function clickButton() {
      console.log("working")
      const shoppingList = document.getElementById("shopping-list");
      const newItem = document.createElement("div");
      newItem.innerHTML = '<div>\n' +
        '<form action="/home/add_item" method="POST" name="listForm" class="listForm">' +
        '<input type="text" name="item" id="item" class="mr-1">' +
        '<input type="submit" value="save item" id="submitItem" class="btn btn-sm submitItem rounded shadow-sm">\n' +
        '</form>' +
        '</div>';
      
      shoppingList.appendChild(newItem);

      $('#submitItem').submit((e) => {
          console.log('click');
          e.preventDefault()
          const form = $('.listForm');
          console.log(form.serialize());
          $.ajax({
              url: form.attr('action'),
              type: form.attr('method'),
              headers: {
                  'Accept': 'application/json',
                  'Content-Type': 'application/json',
                },
              data: {
                  item : $('#item').val()
              },
              success : function(json) {
                  $('#ingredients').val('');
                  console.log(json);
                  console.log('Sucessful!!!');
              }
          })

        });
    });
    $('[data-toggle="tooltip"]').tooltip();
    });
   

    // $('#addIngredient').click(() => {
    //         const ingredients = document.getElementById("ingredients");
    //         const div = document.createElement("div");
    //         div.innerHTML = '<div>\n' +
    //             '<form action="/home/add_ingredient" method="POST" name="ingredientForm" class="ingredientForm">' +
    //             '<label for="quantity" class="mr-1">Amount: </label>' +
    //             '<input type="text" name="quantity" id="quantity" class="mr-1">' +
    //             '<select name="measurement" id="measurement" class="mr-1">' +
    //             '<option value="tsp">tsp.</option>' +
    //             '<option value="tbsp">tbsp.</option>' +
    //             '<option value="fl-oz">fl oz</option>' +
    //             '<option value="mL">mL</option>' +
    //             '<option value="cup">cup</option>' +
    //             '<option value="ounce">oz</option>' +
    //             '<option value="lb">lb</option>' +
    //             '<option value="g">g</option>' +
    //             '</select>' +
    //             '<label for="name" class="mr-1">Name: </label>' +
    //             '<input type="text" name="name" id="name" class="mr-1">' +
    //             '<input type="submit" value="save ingredient" id="submitIngredient" class="submitIngredient rounded shadow-sm bg-white rounded">\n' +
    //             '</form>' +
    //             '</div>';
    //         ingredients.appendChild(div);

            

    //         $('#submitIngredient').submit((e) => {
    //             console.log('click');
    //             e.preventDefault()
    //             const form = $('.ingredientForm');
    //             console.log(form.serialize());
    //             $.ajax({
    //                 url: form.attr('action'),
    //                 type: form.attr('method'),
    //                 headers: {
    //                     'Accept': 'application/json',
    //                     'Content-Type': 'application/json',
    //                   },
    //                 data: {
    //                    quantity : $('#quantity').val(),
    //                    measurement : $('#measurement').val(),
    //                    name : $('#name').val()
    //                 },
    //                 success : function(json) {
    //                     $('#ingredients').val('');
    //                     console.log(json);
    //                     console.log('Sucessful!!!');
    //                 }
    //             })
    //             // .done(function(response){
    //             //     console.log(response);
    //             // })
    //         });
    //     });
    // $('#addStep').click(() => {
    //     const steps = document.getElementById("steps");
    //     const newStep = document.createElement("div");
    //     const stepNum = z;

    //     newStep.innerHTML = '<div>\n' +
    //       '<form action="/home/add_step" method="POST" class="stepForm">' +
    //       '<p class="mr-1 d-inline">' + stepNum + '.</p>' +
    //       '<input type="text" name="step" id="step" class="mb-1 mr-1">' +
    //       '<input type="hidden" name="step_number" id="step_number" value="' + stepNum + '">' +
    //       '<input type="submit" value="save step" class="submitStep rounded shadow-sm bg-white rounded">\n' +
    //       '</form>\n' +
    //       '</div>';
        
    //     steps.appendChild(newStep);
    //     z++;

    //     $('.submitStep').submit((e) => {
    //         console.log('click');
    //         e.preventDefault()
    //         const form = $('.stepForm');
    //         console.log(form.serialize());
    //         $.ajax({
    //             url: form.attr('action'),
    //             type: form.attr('method'),
    //             headers: {
    //                 'Accept': 'application/json',
    //                 'Content-Type': 'application/json',
    //               },
    //             data: {
    //                 step : $('#step').val(),
    //                 step_number : $('#step_number').val(),
    //             },
    //             success : function(json) {
    //                 $('#ingredients').val('');
    //                 console.log(json);
    //                 console.log('Sucessful!!!');
    //             }
    //         });
    //     });
    // }); 

// function getCookie(c_name) {
//                   if(document.cookie.length > 0) {
//                       c_start = document.cookie.indexOf(c_name + "=");
//                       if(c_start != -1) {
//                           c_start = c_start + c_name.length + 1;
//                           c_end = document.cookie.indexOf(";", c_start);
//                           if(c_end == -1) c_end = document.cookie.length;
//                           return unescape(document.cookie.substring(c_start,c_end));
//                       }
//                   }
//                   return "";
//               }
  