
var amountCookies = document.querySelector('.count').innerText;

console.log( amountCookies > 0);

if(amountCookies < 5){
    setTimeout(function() {
        document.querySelector('.count').innerText = 5;
    }, 2000);    
}