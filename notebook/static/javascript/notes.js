const form = document.querySelector(".addEntry")
const open = document.querySelector(".newEntry");
const close = document.querySelector(".close");
const addButton = document.querySelector(".addButton")
const cards = document.querySelector(".card")
let formId = document.querySelector(".noteId");
let formName = document.querySelector(".noteTitle");
let formText = document.querySelector(".noteText");

open.addEventListener("click", () =>{
    form.classList.remove("hidden");
    form.classList.add("show");
	addButton.classList.add("hidden");
	cards.classList.add("hidden");

});

close.addEventListener("click", () => {
    form.classList.remove("show");
    form.classList.add("hidden");
	addButton.classList.remove("hidden");
	cards.classList.remove("hidden");

});

function edit(callId, callName, callText){
    form.classList.remove("hidden");
    form.classList.add("show");
	addButton.classList.add("hidden");
	cards.classList.add("hidden");

    formId.value = callId;
    formName.value = callName;
    formText.value = callText;
};
