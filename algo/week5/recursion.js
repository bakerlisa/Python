function binarySearch(arr,val){
    let middle = Math.floor((arr.length -1) / 2);


    if (arr.length == 0) {
        return "false"
    } 
 
    if(arr[middle] == val){
        return "true"
    }else if(val < arr[middle]){
        console.log(arr.slice(0, middle))
        return binarySearch(arr.slice(0, middle), val)
    }else{
        console.log(arr.slice(middle + 1, arr.length))
        return binarySearch(arr.slice(middle + 1, arr.length), val)
    }
}

console.log(binarySearch([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],-9))
// binarySearch([1, 2],2)
// binarySearch([1, 2],4)
// binarySearch([1,2,2],2)
// binarySearch([],7)
// binarySearch([1,2,2,2,2,2,2,4,5,5,5,5,6,6,6],2)
// binarySearch([1,1,1,1,1],1)

// binarySearch([1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 8, 9, 10,11],2)




// ANSWER
// function recursiveBinarySearch(arr, val) {
//     let middle = Math.floor((arr.length - 1) / 2);
//     if (arr.length == 0) {
//         return false
//     }
//     if (arr[middle] == val) {
//         return true
//     } else if (val < arr[middle]) {
//         console.log("chekcing middle " + middle)
//         console.log("checking left")
//         return recursiveBinarySearch(arr.slice(0, middle), val)
//     } else {
//         console.log("chekcing middle " + middle)
//         console.log("checking right")
//         return recursiveBinarySearch(arr.slice(middle + 1, arr.length), val)
//     }
// }
