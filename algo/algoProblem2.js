function isLongestPalliTakeTwo(pallis){
    var longestWord = "";
    var word;

    //starts to loop through our string
    for(target=0;target<pallis.length;target++){
        // sets up left an right to our target value, so we can compare based on our target.
            //target is curent element of the string we're looing at. first time its m, 2nd y ect.
        var left = target - 1;
        var right = target + 1;

        //compares left and right values
        if(pallis[right] == pallis[left]){
            //if both left and right of our trage matches
            var innerLeft = target - 1; 
            var innerRight = target + 1;

            // we want to stay on our target, but see how far the palldirum goes. So we hop into another for loop till it returns false
            //doing the same checks as we did above
            for(u=0; target > u; u++){
                if(pallis[innerLeft] == pallis[innerRight]){
                    if(u == 0){    
                        word = pallis[innerLeft]+pallis[target]+pallis[innerRight];
                    }else{
                        word = pallis[innerLeft] + word + pallis[innerRight];
                    }
                    //increment our left and right, target stays the same
                    innerRight++;
                    innerLeft--;
                }else{
                    break;
                }
            }
        //if the target is the first element
        }else if(pallis[target] == pallis[right]){
            word = pallis[target] + pallis[right]; 
            continue;
        //if the target is the last element
        }else if(pallis[target] == pallis[left]){
            word = pallis[target] + pallis[left]; 
            continue;
        }

        // checks palli word we just found, compares to current longestWord, if our new word is longer, it resets the longestWord to word, else it keeps our current longest word
        if(word.length > longestWord.length){    
            longestWord = word;
        }
        //clears word
        word;
    }
    return longestWord;
}

console.log(isLongestPalliTakeTwo("mm favorite racecar erupted"));