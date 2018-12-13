var req;
function getFortune() {

    if (window.XMLHttpRequest) {
        req = new XMLHttpRequest();
    } else {
        req = new ActiveXObject("Microsoft.XMLHTTP");
    }
    req.onreadystatechange = handleResponse;
    req.open("GET", "https://garrod.isri.cmu.edu/webapps/fortune/", true);
    req.send();
}

function handleResponse() {
    if (req.readyState != 4 || req.status != 200) {
        return;
    }
    var x = document.getElementById("content");
    // x.innerText = this.responseText;
    x.innerHTML = this.responseText;
}