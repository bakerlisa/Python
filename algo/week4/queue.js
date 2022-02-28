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
        this.tail = null
    }

    // remove and return the front value from the queue
    dequeue(value) {
        var newNode = new Node(value);

        if(this.head == null) {
            // theres no head so set the head to new node
            this.head = newNode;
            return this;
        }else{
            //else set new node as head and next to old head
            newNode.next = this.head;
            this.head = newNode;
            return this;
        }
    }
    

    // add a node with the given value to the queue / addToBack
    enqueue(value) {
        var newNode = new Node(value);

        if(this.head == null) {
            // only one val means that's our head
            this.head = newNode;
            this.tail = newNode;
            return this;
        }else{
            //if we have a head but no next, set the head's next value
            var runner = this.head;
            if(runner.next == null){
                this.head = newNode;
            }else{
            //if we have a head and it has a next, start looping to find the end
            //not sure if we need this, or can combine it with the if statment, but here we are
                while(runner.next.next){
                    runner = runner.next
                }
                runner = newNode.next;
                this.tail = newNode;
                return this;
            }
        }
    }
    
    // remove the minimum value in the queue (remember your edgecases and pointers!)/ findMin
    removeMin(){
        var lowest = this.head.value;
        var runner = this.head;
        var perviousCurrent = this.head;
        
        // Finding lowest value
        //pushes off to the end so we can check last value
        while(runner != null){
            if(runner.value < lowest){
                // saving lowest value
                lowest = runner.value;
            }else{
                perviousCurrent = runner;
            }

            runner = runner.next;
        }
        //Finish this


        // reseting value
        runner = this.head;
        var pervious = this.head;
        while(runner.value != lowest){
            pervious = runner;
            runner = runner.next;
        }
        if(pervious == runner){
            //benging
            this.head = runner.next;
            runner.next = runner.next.next;
        }else if(runner.next == null){
            //middle
            pervious.next = null;
            pervious.next = this.tail
        }else{
            //end
            pervious.next = runner.next
        }
        return this
    }

    contains(value){
        var newNode = new Node(value);
        var runner = this.head;
        if(!this.head){

        }
        while(runner != null){
            if(runner.value == value){
                return true;
            }
            runner = runner.next;
        }
        return false;
    }
    
    displayQueue(value,loc){
        var newNode = new Node(value);
        var runnerCounter = 1;
        var runner = this.head;

        while(runner.next != null){
            if(runnerCounter == 1){
                this.head = this.head.next;
            }
            runnerCounter++;
            runner = runner.next;
        }
        runner.next = newNode;
        this.tail = newNode;

        var findVal = runnerCounter - loc;
        
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
sll.dequeue(10);
sll.dequeue(70);
sll.dequeue(60);
sll.dequeue(40);
sll.dequeue(100);
sll.dequeue(30);
sll.dequeue(20);
sll.dequeue(223);


sll.removeMin()

sll.printValues();

