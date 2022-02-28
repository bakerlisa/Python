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
            // only one val means that's our head
            this.head = newNode;
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
                return this;
            }
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

    findMin(){
        // var runnerPrevious;
        // runnerPrevious = runner;
        var lowest = this.head.value;
        var runner = this.head;
        var perviousCurrent = this.head;
        // console.log(this.head);
        
        // Finding lowest value

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
        var runner2 = this.head;
        
        while(runner2.value != lowest){
            // console.log(runner2.value );
            runner2 = runner2.next;
        }

        return this
    }

    appendValue(value,loc){
        var newNode = new Node(value);
        var runner = this.head;
        var counter = 1;

        while(runner != null){
            if(loc <= 0){
                //at the begining: set to head
                this.head = newNode;
                newNode.next = runner;
                break;
            }else if(counter == loc){
                var temp = runner.next;
                runner.next = newNode;
                newNode.next = temp;
                break;
            }else if(runner.next == null){
                //at the end: set it to tail
                runner.next = newNode;
                break;
            }
            runner = runner.next;
            counter++;
        }
    }

    prependValue(value,loc){   
        var newNode = new Node(value);
        var runner = this.head;
        var counter = 1;
        var minusOnLocal = loc - 1;

        while(runner != null){
            if(minusOnLocal <= 1){
                //at the begining: set to head
                this.head = newNode;
                newNode.next = runner;
                break;
            }else if(counter == minusOnLocal){
                //in the middle
                var temp = runner.next;
                runner.next = newNode;
                newNode.next = temp;
                break;
            }else if(runner.next == null){
                //at the end: set it to tail
                runner.next = newNode;
                break;
            }
            runner = runner.next;
            counter++;
        }
    }

    prependValueBehind(value,loc){
        var newNode = new Node(value);
        var runnerCounter = 1;
        var runner = this.head;

        while(runner.next != null){
            runnerCounter++;
            runner = runner.next;
        }

        var findVal = runnerCounter - loc + 1;
        var NewRunner = this.head;
        var counter = 1;
        var temp;
        
        while(NewRunner != null){
            if(findVal <= 0){
                this.head = newNode;
                newNode.next = NewRunner;
                break;
            }else if(counter == findVal){
                temp = NewRunner.next;
                NewRunner.next = newNode;
                newNode.next = temp;
                break;
            }else if(runnerCounter < findVal){
                runner.next = newNode;
                break;
            }
            counter++;
            NewRunner = NewRunner.next;
        }
    }

    appendValuesBehind(value,loc){
        var newNode = new Node(value);
        var runnerCounter = 1;
        var runner = this.head;

        while(runner.next != null){
            runnerCounter++;
            runner = runner.next;
        }

        var findVal = runnerCounter - loc;
        var NewRunner = this.head;
        var counter = 1;
        var temp;
        
        while(NewRunner != null){
            if(findVal <= 0){
                this.head = newNode;
                newNode.next = NewRunner;
                break;
            }else if(counter == findVal){
                temp = NewRunner.next;
                NewRunner.next = newNode;
                newNode.next = temp;
                break;
            }else if(runnerCounter < findVal){
                runner.next = newNode;
                break;
            }
            counter++;
            NewRunner = NewRunner.next;
        }
    }

    queue(value,loc){

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
sll.addToFront(80);
sll.addToFront(70);
sll.addToFront(60);
sll.addToFront(40);
sll.addToFront(30);
sll.addToFront(20);
sll.addToFront(10);

sll.queue(50)

sll.printValues();

// sll.findMin();