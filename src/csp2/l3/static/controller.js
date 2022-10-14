function chooseTab(num) {
    // Dynamically load the appropriate image.
    var html = "Image " + parseInt(num) + "<br>";
    html += "<img src='/static/level3/cloud" + num + ".jpg' />";
    $('#tabContent').html(html);

    window.location.hash = num;
    // Select the current tab
    var tabs = document.querySelectorAll('.tab');
    for (var i = 0; i < tabs.length; i++) {
        if (tabs[i].id == "tab" + parseInt(num)) {
            tabs[i].className = "tab active";
        } else {
            tabs[i].className = "tab";
        }
    }
    // Tell parent we've changed the tab
    top.postMessage(self.location.toString(), "*");
}

window.onload = function() {
    chooseTab(unescape(self.location.hash.substr(1)) || "1");
}

// Extra code so that we can communicate with the parent page
window.addEventListener("message", function(event){
    if (event.source == parent) {
        num = unescape(parseInt(self.location.hash.substr(1)))
        if ((num == 1) || (num == 2) || (num == 3)) {chooseTab(num)}
        else {chooseTab(1)}
    }
}, false);


tb1 = document.getElementById("tab1");
tb1.addEventListener('click', function(){chooseTab(1)}, false);
tb2 = document.getElementById("tab2");
tb2.addEventListener("click", function(){chooseTab(2)}, false);
document.getElementById("tab3").addEventListener("click", function(){chooseTab(3)});