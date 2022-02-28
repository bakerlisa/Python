function binarySearch(arr,val){

    var totalLength = Math.floor(arr.length - 1) / 2;
    console.log("totalLength: " + totalLength)
    console.log(arr[totalLength])
    
    if(arr[totalLength] == val){
        
    }else{
        return -1
    }
}

// console.log(binarySearch([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],19))
// console.log(binarySearch([1, 2],2))
// console.log(binarySearch([1, 2],4))
// console.log(binarySearch([1,2,2],2))
// console.log(binarySearch([],7))
// console.log(binarySearch([1,2,2,2,2,2,2,4,5,5,5,5,6,6,6],2))
// binarySearch([1,1,1,1,1],1)
var arrRcurrsion = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 8, 9, 10]
console.log(binarySearch(arrRcurrsion,8))