// REVERSESTRING
// version1:
// function reverse(element){
//     var eleArr = element.split('');
//     var reversed = [];
//     for(i=element.length - 1; 0 <= i; i--){
//         reversed += element[i];
//     }
//     return reversed;
// }
// console.log(reverse('broadhead'));

// version2:
// function reverse(element){
//     var reversed = "";
//     for(i = element.length - 1; 0 <= i; i--){
//         reversed += element[i];
//     }
//     return reversed;
// }
// console.log(reverse('broadhead'));


// ACRONYM
// Goal - "Welcome to Python" = "WTP"

// version1
// function acronym(element){
//     var splitElement = element.split(' ');
//     var acronym = [];
    
//     for(var i=0; i < splitElement.length; i++){
//         var wordSplit = splitElement[i].split('');
//         acronym.push(wordSplit[0]);
//     }
//     return acronym;  
// }
// console.log(acronym("Coding Is Awesome").join(''));

// // version2
function acronym(element){
    var acronym = "";

    for(j=0; j < element.length; j++){
        if(element[j] == " " && element[j+1] != '-'){
            acronym += element[j+1];
        }else if( j == 0){
            acronym += element[j];
        } 
    }
    return acronym;  
}
console.log(acronym("there's no free lunch - gotta pay yer way"));