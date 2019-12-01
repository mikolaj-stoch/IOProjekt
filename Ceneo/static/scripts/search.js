function validateForm(){
    var emptyFields = 0;
    for(var i=0; i<5; i++){
        var productName = document.forms["inputForm"]["productName" + i].value;
        var quantity = parseInt(document.forms["inputForm"]["quantity" + i].value);
        var minPrice = parseInt(document.forms["inputForm"]["minPrice" + i].value);
        var maxPrice = parseInt(document.forms["inputForm"]["maxPrice" + i].value);

        if (!productName){
            emptyFields++;
        }

        if (!productName && quantity > 0){
            displayAlert("Enter the name of product no " + (i+1) + " or set quantity to 0.");
            return false;
        }

        if (productName && !quantity){
            displayAlert("Enter the quantity of product no " + (i+1) + ".");
            return false;
        }

        if ((minPrice > maxPrice) && maxPrice){
            displayAlert("Minimum price of product no " + (i+1) + " is higher than maximum.");
            return false;
        }
    }

    if(emptyFields == 5){
        displayAlert("Enter at least one product.");
        return false;
    }

    return true;
}

function displayAlert(msg){
    var alertBox = document.getElementById("alert");
    var message = document.getElementById("message");
    alertBox.style.display = 'block';
    message.innerHTML = msg;
}