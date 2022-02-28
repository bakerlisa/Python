// is a palli and which is longest!
// function isPalli(pall){
//     longestPalli = "!";
//     var isPalli = false;

//     for(i=0; i < pallis.length;i++){
//         for(j=0;j<pallis[i].length / 2;j++){
//             var lastPalliChar = pallis[i][pallis[i].length - 1 - j];
//             var firstPalliChar = pallis[i][j]

//             // this skips white space
//             if(firstPalliChar == " " || lastPalliChar == " "){
//                 continue;
//             //checks first and last char
//             }else if(firstPalliChar == lastPalliChar){
//                 isPalli = true;
//             }else{
//                 isPalli = false;
//             }
//         }
//         //outside of 2 for loop: checks palli len
//         if(isPalli){
//             console.log(`🎉 ${pallis[i]}`)
//             // checking for longest palli
//             if(longestPalli.length < pallis[i].length){
//                 longestPalli = pallis[i]
//             }
//         }else{
//             console.log(`🤔 Hmmm "${pallis[i]}" it trying to masquerade as a palli!`)
//         }
//     }
//     console.log(`🥇 ${longestPalli}: Is the winner for longest Palli`)
// }

// var pallis = ["a man", "tacocat","racecar","madam I'm adam","rats live on no evil star", "I'm a palli I swear"]

// function isAPalli(pallis){
//     var isPalli = false;

//     for(j=0;j<pallis.length / 2;j++){
//         var lastPalliChar = pallis[pallis.length - 1 - j];
//         var firstPalliChar = pallis[j];

//         // this skips white space
//         if(firstPalliChar == " " || lastPalliChar == " "){
//             continue;
//         //checks first and last char
//         }else if(firstPalliChar === lastPalliChar){
//             isPalli = true;
//         }else{
//             return false;
//         }
//     }
//     return isPalli;
// }
// console.log(isAPalli("oho!"));

// function isLongestPalli(pallis){
//     var isSentancePalli;
//     var longestWordAPalli = " ";
    
//     //looks at sentance
//     for(i=0; i < pallis.length;i++){
//         for(j=0;j<pallis[i].length / 2;j++){
//             //checks  each word
//             var lastPalliChar = pallis[i][pallis[i].length - 1 - j];
//             var firstPalliChar = pallis[i][j];
//             // this skips white space
//             if(firstPalliChar == " " || lastPalliChar == " "){
//                 continue;
//             //checks first and last char
//             }else if(firstPalliChar == lastPalliChar){
//                 isSentancePalli = true;
//             }else{
//                 isSentancePalli = false;
//             }
//         }
//     }

//     //looks at the words
//     var word = "";
//     var sentance = [];
    
//     for(i=0; i < pallis.length;i++){
//         for(j=0;j<pallis[i].length;j++){
//             var lastChar = pallis[i][pallis[i].length - 1];
//             var lastPalliChar = pallis[i][pallis[i].length - 1 - j];
//             var firstPalliChar = pallis[i][j];

//              //chekcing words
//             if(firstPalliChar !== " " ){
//                 //word.push(pallis[i][j])
//                 word += pallis[i][j];
//             }else{
//                 sentance.push(word);
//                 word = "";
//                 continue;
//             }
//         }
//     }
//     for(k=0;k<sentance.length;k++){
//         for(l=0;l<sentance[k].length / 2;l++){
//             var lastSentanceChar = sentance[k][sentance[k].length - 1 - l];
//             var firstSentanceChar = sentance[k][l];
            
//             if(firstSentanceChar == lastSentanceChar){
//                 longestWordAPalli = sentance[k];
//             }
//         }
//     }
//     sentance.push(word);
//     word = "";
//     console.log(longestWordAPalli);
// }

// // console.log(isLongestPalli("my favorite racecar erupted"));
// isLongestPalli("my favorite racecar erupted");

// Given a String, return the longest pallindromic substring. Given "hello dada", return "dad". Given "not much" return "n". Include spaces as well!

// Example 1: "my favorite racecar erupted" --> "e racecar e"
// Example 2: "nada" --> "ada"
// Example 3: "nothing to see" --> "ee"

function isLongestPalliTakeTwo(pallis){
    var longestWord = " ";
    var word = "";

    //starts to loop through our string
    for(t=0;t<pallis.length;t++){
        // sets up left an right to our target value, so we can compare
        var left = t - 1;
        var right = t + 1;

        //compares left and right values
        if(pallis[right] == pallis[left]){
            //if both left and right of our trage matches
            var innerLeft = t - 1; 
            var innerRight = t + 1;

            // we want to stay on our target, but see how far the palldirum goes. So we hop into another for loop till it returns false
            //doing the same checks as we did above
            for(u=0; t > u; u++){
                if(pallis[innerLeft] == pallis[innerRight]){
                    if(word.length == 0){    
                        word = pallis[innerLeft]+pallis[t]+pallis[innerRight];
                    }else{
                        word = pallis[innerLeft] + word + pallis[innerRight];
                    }
                    //increment our left and right, target stays the same
                    innerRight++;
                    innerLeft--;
                }else{
                     // checks current largest to current word, if current word is larger it updates currentLargest
                    if(word.length > longestWord.length){  
                        longestWord = word;
                    }
                    word = " ";
                    break;
                }
            }
        //if the target is the last element
        }else if(pallis[t] == pallis[right]){
            //push first and right
            word = pallis[t] + pallis[right]; 
            if(word.length > longestWord.length){    
                longestWord = word;
            }
            continue;
        //if the target is the first element
        }else if(pallis[t] == pallis[left]){
            // iterator and last
            word = pallis[t] + pallis[left]; 
            if(word.length > longestWord.length){    
                longestWord = word;
            }
            continue;
        }else{
            if(word.length > longestWord.length){
                // resets my values
                longestWord = word;
            }
            word = "";
            continue;
        }
    }
    return longestWord;
}

console.log(isLongestPalliTakeTwo("mm favorite racecar erupted"));