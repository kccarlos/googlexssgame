var loadimg = document.getElementById("loading");
let countdown = document.getElementsByName('seconddata')[0].content;

loadimg.onload = function startTimer(seconds) {
    console.log(seconds)
    countdown = parseInt(countdown) || 3;
    setTimeout(function () {
        console.log(countdown)
        window.confirm("Time is up!");
        window.history.back();
        }, countdown * 1000);

    }
