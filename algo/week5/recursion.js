function binarySearch(arr,val){
    var arrHalf = Math.floor(arr.length  / 2);
    if(arrHalf == 1){
        if(arr[0] === val || arr[1] === val){
            console.log(val)
        }else{
            console.log( "-1")
        }
    }else if(arr[arrHalf] == val){
        console.log(val)
    }else if(arr[arrHalf] > val){
        var newArr = arr.slice(0,arr[arrHalf]);
        binarySearch(newArr,val)
    }else if(arr[arrHalf] < val){
        var newArr =  arr.slice(arr[arrHalf],(arr.length));
        binarySearch(newArr,val)
    }else{
        console.log( "-1")
    }   
}

console.log(binarySearch([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],19))
// binarySearch([1, 2],2)
// binarySearch([1, 2],4)
// binarySearch([1,2,2],2)
// binarySearch([],7)
// binarySearch([1,2,2,2,2,2,2,4,5,5,5,5,6,6,6],2)
// binarySearch([1,1,1,1,1],1)

// binarySearch([1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 8, 9, 10,11],2)