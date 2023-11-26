const form = document.querySelector(".addEntry")
const open = document.querySelector(".newEntry");
const close = document.querySelector(".close");
let formId = document.querySelector(".noteId");
let formName = document.querySelector(".noteTitle");
let formText = document.querySelector(".noteText");

open.addEventListener("click", () =>{
    form.classList.remove("hidden");
    form.classList.add("show");

});

close.addEventListener("click", () => {
    form.classList.remove("show");
    form.classList.add("hidden");
});

function edit(callId, callName, callText){
    form.classList.remove("hidden");
    form.classList.add("show");

    formId.value = callId;
    formName.value = callName;
    formText.value = callText;
};