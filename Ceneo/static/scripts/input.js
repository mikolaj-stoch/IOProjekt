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
            window.alert("Enter the name of product no " + (i+1) + " or set quantity to 0.");
            return false;
        }

        if (productName && !quantity){
            window.alert("Enter the quantity of product no " + (i+1) + ".");
            return false;
        }

        if ((minPrice > maxPrice) && maxPrice){
            window.alert("Minimum price of product no " + (i+1) + " is higher than maximum.");
            return false;
        }
    }

    if(emptyFields == 5){
        window.alert("Enter at least one product.");
        return false;
    }

    return true;
}