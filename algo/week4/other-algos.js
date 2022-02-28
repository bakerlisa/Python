// var number = 20;
// var display = function(){
//     console.log(number);
//     var number = 10;
// }
// display();

class Node{
    constructor(vlaue){
        this.value = this.value
        this.next = null
    }
}

class SLList{
    constructor(){
        this.head = null
    }

    addtToFront(value){
        //step #1 Make a new node
        var newNode = new Node(value);

        //check to see if there is a head
        if(this.head == null){
            this.head = newNode;
            return this;
        }

        // if there is a head
        newNode.next = this.head;
        this.head = newNode;

        return this
    }
}