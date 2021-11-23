const cbox = document.querySelectorAll(".content-box");

 
for (let i = 0; i < cbox.length; i++) {
    cbox[i].addEventListener("mouseover","onClick", function() {
    cbox[i].classList.add("active");
});
}

for (let i = 0; i < cbox.length; i++) {
    cbox[i].addEventListener("mouseout","onClick", function() {
    cbox[i].classList.remove("active");
});
}








