//Simple 
function parensValid(str){
    var valid = false;
    for(i=0;i<str.length; i++){
        if(str[i] == "("){    
            valid =  false;
        }else if(str[i] == ")"){
            valid = true;
        }
    }
    return valid;
}
// function call
console.log(parensValid("This is a (string )this is a string"));


// Complex
function bracesValid(str){
    var inStr = [];
    var elements = ["(",")","{","}","[","]"];
    //cleans string, to only items interested in
    for(i=0;i<str.length; i++){
        for(k=0;k<elements.length;k++){
            if(str[i] == elements[k]){
                inStr.push(elements[k]);
            }
        }
    }

    // switch: on/off 
    var valid;

    // odd: automatically false 
    if(inStr.length % 2 == 0){
        for(b = 0; b < inStr.length / 2; b++){
            // loops element char and compares them to the 1 char in inStr
            for(e = 0; e < elements.length; e++){
                // If first:opening == last:closing, or the first:opening == nextTo:closing then valid = true
                if(inStr[inStr.length - 1 - b] == elements[e + 1] && inStr[inStr.length - 1 - b] == elements[e +1]  || inStr[b] == elements[e+1]){
                    valid = true;
                }
            }
        }
    }else{
        return false;
    }
    return valid;
}

// console.log(bracesValid("({[({})]})"));
// console.log(bracesValid("d(i{a}l[t]o)n{e!"));
console.log(bracesValid("{{[a]}}(){bcd}{()}"));

// Example 1: "({[({})]})" --> true
// Example 2: "d(i{a}l[t]o)n{e!" --> false
// Example 2: "{{[a]}}(){bcd}{()}" --> true