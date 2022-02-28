// function bookIndex(arr){

//     var read = [];

//     for(i=0; i < arr.length;i++){
//         var startVal;
//         var endVal;
//         console.log(arr[i])
//         if(arr[i] + 1 == arr[i + 1]){
//             //the next number is not out of our arr and target value == next targe value
//             startVal = arr[i];
//             // console.log(startVal)
//             var counter = 2;
//             for(j=arr[i];j<arr.length;j++){

//                 if(arr[j] + counter ==  arr[j + counter]){
//                     counter++;
//                 }else{
//                     endVal = arr[j];
//                     //update the arr
//                     read.push(startVal + " - " + endVal)
//                     //clear vlaues
//                     startVal = 0;
//                     endVal = 0;
//                     // reset i so we don't go back over numbers in our range
//                     i = j;
//                     break;

//                 }
//             }
// //look at the blaues in where counter is looking at target of + 1 target +2 
//         }else{
//             //non consecutive

//             read.push(arr[i]); 
//         }
//     }
//     return read;
// }


function bookIndex(arr){
    var startRange;
    var counter;
    var counterTwo = 1;
    var readRange = [];
    for(i=0; i < arr.length;i++){
        if(arr[i] + 1 == arr[i + 1]){
            startRange = arr[i]
            counter = i;
            for(j=counter; j < arr.length; j++){
                if(startRange + counterTwo == arr[j + counterTwo]){
                    counterTwo += 1;
                    continue; 
                }else{
                    i = j + 1;
                    readRange.push(startRange + " - " + arr[j + 1]);
                    break;
                }
            }
        }else{
            readRange.push(arr[i])
        }
    }
    return readRange;
}
console.log(bookIndex([1,3,4,5,7,8,10,12]))
// bookIndex([1,3,4,5,7,8,10,12])