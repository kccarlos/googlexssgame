var loadimg = document.getElementById("loadimg");
let countdown = document.getElementsByName('seconddata')[0].content;
loadimg.onload = function startTimer(seconds) {
    countdown = parseInt(countdown) || 3;
    setTimeout(function () {
        window.confirm("Time is up!");
        window.history.back();
    }, countdown * 1000);
}