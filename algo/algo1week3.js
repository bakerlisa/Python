// Singly Linked List
class Node{
    constructor(value){
        this.value = value
        this.next = null
    }
}

class SLList{
    constructor(){
        this.head = null
    }

    addToFront(value) {
        var newNode = new Node(value);

        if(this.head == null) {
            this.head = newNode;
            return this;
        }else{
            newNode.next = this.head;
            this.head = newNode;
            return this;
        }
    }

    addToBack(value) {
        var newNode = new Node(value);
        
        if(this.head == null) {
            //sets the head
            this.head = newNode;
            return this;
        }else if(this.head.next == null){
            //sets the heads next val
            this.head.next = newNode
        }else{
            var runner = this.head;
            while(runner.next != null){
                runner = runner.next;
            }
            runner.next = newNode;
            return this;
        }
    }

    removeFromFront() {
        //if there's no head, there's no list
        if(this.head.next != null){  
            this.head = this.head.next;
        }
        return this
    }

    removeFromBack() {
        var runner = this.head;
        
        if(runner.next == null){
            //only 2 values left; unconnect head and 2nd val
            this.head.next = null;
        }else{
            // 3 > loop to find end
            while(runner.next.next != null){
                runner = runner.next;
            }
            runner.next = null;
        }
        return this
    }

   // print the singly linked list
    printValues() {
        // step #0 [EDGE CASE]) handle a case where there is nothing in the list
        if(this.head == null){
            console.log("There's nothing in the list! Dummy!")
            // return 'this' to end function and allow chaining of methods
            return this
        }
        //step #1) establish a runner to traverse through the list
        var runner = this.head;

        // NOTE: we can move runner all the way into null because our loop will exit as soon as runner hits null, avoiding any errors with printing
        while(runner != null) {
            // step #2) print the values at each iteration before moving the runner!
            console.log(`The current value is: ${runner.value}`)
            runner = runner.next
        }
        
        console.log("We have hit the end of the list!")
        // return 'this' to end function and allow chaining of methods
        return this
    }   
}


var sll = new SLList();
// sll.addToFront(64);
// sll.addToFront(92);
// sll.addToFront(45);

sll.printValues()

function contains(val){
    var runner = sll.head;

    while(runner != null){
        if(runner.value == val){
            return true;
        }
        runner = runner.next;
    }
    return false;
}
console.log(contains(0));

