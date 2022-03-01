function recursiveGreatestCommonFactor(val1,val2){
    var mod = val1 % val2;
    console.log(` mod : ${mod}`)

    if(val1 % val2 == 2){
        val1 -= mod;
        val2 -= mod;
    }

    console.log(val1)
    console.log(val2)

    if(val1 === val2 || mod == 0 ){
        return val1;
    }else if(val1 > val2){
        val1 -= val2
        return recursiveGreatestCommonFactor(val1,val2)
    }else if(val1 < val2){
        val2 -= val1
        return recursiveGreatestCommonFactor(val1,val2)
    }
}


// console.log(recursiveGreatestCommonFactor(50,180)); // 10
// console.log(recursiveGreatestCommonFactor(7,35)); // 7
// console.log(recursiveGreatestCommonFactor(65,95)); // 5
// console.log(recursiveGreatestCommonFactor(123456,987654)); // 6
console.log(recursiveGreatestCommonFactor(102,1000)); // 2
// console.log(recursiveGreatestCommonFactor(7,13)); // 1


// ANSWER
// function recursiveBinarySearch(arr, val) {
//     let middle = Math.floor((arr.length - 1) / 2);
//     if (arr.length == 0) {
//         return false
//     }
//     if (arr[middle] == val) {
//         return true
//     } else if (val < arr[middle]) {
//         return recursiveBinarySearch(arr.slice(0, middle), val)
//     } else {
//         return recursiveBinarySearch(arr.slice(middle + 1, arr.length), val)
//     }
// }
