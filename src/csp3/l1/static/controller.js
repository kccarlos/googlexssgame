if (document.getElementById("query")){
    query = document.getElementById("query");
    query.addEventListener('focus', myfunction);
}

function myfunction() {
    document.getElementById("query").value = "";
}