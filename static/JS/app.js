// home boxes mouse hover 
const cbox = document.querySelectorAll(".content-box");


for (let i = 0; i < cbox.length; i++) {
    cbox[i].addEventListener("mouseover", function() {
    if (cbox[i] !== cbox[0]){
    cbox[i].classList.add("active");
    cbox[0].classList.remove("active");
    }else{
        cbox[0].classList.add("active");
    }});
}

for (let i = 0; i < cbox.length; i++) {
    cbox[i].addEventListener("mouseout", function() {
    if (cbox[i] !== cbox[0]){
    cbox[i].classList.remove("active");
    cbox[0].classList.add("active");
    }else{
        cbox[0].classList.add("active");
    }});
}



// home box prev/next cycle

//variables
let nextBtn = document.querySelector(".next-btn");
let prevBtn = document.querySelector(".prev-btn");
let box = document.querySelectorAll(".content-box");
let listLength = box.length - 1;

// Set up counter
let count = (function(){
    //index inital value
    let counter = 0;
    // function changes value positive or negative
    function changeBy(val){
        counter+=val;
    }

    return {
        countUp: function() {
            changeBy(1);
        },
        countDown: function() {
            changeBy(-1);
        },
        // holds the new counter value
        value: function() {
            return counter;
        }
    };
})();
console.log(box.length);

function selectNext() {
    // current index in counter
    let currentIndex = count.value();

    // sets index at one instead of 0
    currentIndex = currentIndex + 1;

    //moves to next index on click
    count.countUp();
    console.log(currentIndex);
    console.log(listLength);
    
    // Adds class to div
    if (box[currentIndex] !== undefined) {
        box[currentIndex].classList.add("active");
    }
        // Removes class from previous div
    if (box[currentIndex - 1] !== undefined) {
        box[currentIndex - 1].classList.remove("active");
    }

    if (currentIndex === listLength) {
        nextBtn.setAttribute("disabled", "");
    } else {
        prevBtn.removeAttribute("disabled");
    }
}

function selectPrev() {
    // current index in counter
    let currentIndex = count.value();
    
    // Decrement count value
    count.countDown();
    console.log(currentIndex);

    // Add class to previous box
    if (currentIndex > 0 && box[currentIndex - 1] !== undefined) {
        box[currentIndex - 1].classList.add("active");
    }
    // Remove class
    if (box[currentIndex] !== undefined) {
        box[currentIndex].classList.remove("active");
    }

    if (currentIndex - 1 <= 0) {
        prevBtn.setAttribute("disabled", "");
    } else {
        nextBtn.removeAttribute("disabled");
    }
}

// Event Listener
nextBtn.addEventListener("click", selectNext);
prevBtn.addEventListener("click", selectPrev);



// Carousel 
