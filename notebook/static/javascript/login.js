const denied = document.querySelector(".denied");

setTimeout(() => {
    denied.style.left = parseFloat(getComputedStyle(denied).left) - 300 + 'px';
}, 500);

setTimeout(() => {
    denied.style.left = parseFloat(getComputedStyle(denied).left) + 300 + 'px';
}, 6000);