// var defaultMessage = "Welcome!<br><br>This is your <i>personal</i>"
//     + " stream. You can post anything you want here, especially "
//     + "<span style='color: #f00ba7'>madness</span>.";
var defaultMessage = "Welcome!<br><br>This is your <i>personal</i>"
    + " stream. You can post anything you want here, especially "
    + "madness";

var DB = new PostDB(defaultMessage);

function displayPosts() {
    var containerEl = document.getElementById("post-container");
    containerEl.innerHTML = "";

    var posts = DB.getPosts();
    for (var i=0; i<posts.length; i++) {
        var html = '<table class="message"> <tr> <td valign=top> '
            + '<img src="/static/level2_icon.png"> </td> <td valign=top '
            + ' class="message-container"> <div class="shim"></div>';

        html += '<b>You</b>';
        html += '<span class="date">' + new Date(posts[i].date) + '</span>';
        if (i == 0) encoded = posts[i].message;
        else encoded = posts[i].message.replace(/</g, "&lt;").replace(/>/g, "&gt;");
        html += "<blockquote>" + encoded + "</blockquote";
        html += "</td></tr></table>"
        containerEl.innerHTML += html;
    }
}

window.onload = function() {
    document.getElementById('clear-form').onsubmit = function() {
        DB.clear(function() { displayPosts() });
        return false;
    }

    document.getElementById('post-form').onsubmit = function() {
        var message = document.getElementById('post-content').value;
        DB.save(message, function() { displayPosts() } );
        document.getElementById('post-content').value = "";
        return false;
    }

    displayPosts();
}