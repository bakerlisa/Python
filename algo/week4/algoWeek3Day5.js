function change(money){
    var quarters = 0;
    var dimes = 0;
    var nickles = 0;
    var pennies = 0;

    money *= 100;

    while(money > 0){
        if(money >= 25){
            quarters++;
            money -= 25;
        }else if(money >= 10){
            dimes++;
            money -= 10;
        }else if(money >= 5){
            nickles++;
            money -= 5;
        }else{
            pennies++; 
            money -= 1;
        }
    }

    return `quarters: ${quarters}, dimes ${dimes}, nickles ${nickles}, pennies ${pennies}`;
}

console.log(change(1.97));