function myFunction() {
    var a1 = document.getElementById("a1").value;
    var a2 = document.getElementById("a2").value;
    var a3 = document.getElementById("a3").value;
    var b1 = document.getElementById("b1").value;
    var b2 = document.getElementById("b2").value;
    var b3 = document.getElementById("b3").value;
    var c1 = document.getElementById("c1").value;
    var c2 = document.getElementById("c2").value;
    var c3 = document.getElementById("c3").value;

    if (a1 || a2 || a3 != "") {
        if (a1 == a2 && a2 == a3) {
            alert("Gano el jugador " + a1);
        }
    }
    if (b1 || b2 || b3 != "") {
        if (b1 == b2 && b2 == b3) {
            alert("Gano el jugador " + b1);
        }
    }
    if (c1 || c2 || c3 != "") {
        if (c1 == c2 && c2 == c3) {
            alert("Gano el jugador " + c1);
        }
    }
    if (a1 || b1 || c1 != "") {
        if (a1 == b1 && b1 == c1) {
            alert("Gano el jugador " + a1);
        }
    }
    if (a2 || b2 || c2 != "") {
        if (a2 == b2 && b2 == c2) {
            alert("Gano el jugador " + a2);
        }
    }
    if (a3 || b3 || c3 != "") {
        if (a3 == b3 && b3 == c3) {
            alert("Gano el jugador " + a3);
        }
    }
    if (a1 || b2 || c3 != "") {
        if (a1 == b2 && b2 == c3) {
            alert("Gano el jugador " + a1);
        }
    }
    if (a3 || b2 || c1 != "") {
        if (a3 == b2 && b2 == c1) {
            alert("Gano el jugador " + a3);
        }
    }

    if (a1 && a2 && a3 && b1 && b2 && b3 && c1 && c2 && c3 != "") {
        alert("Empate");
    }

}
function clearInput(){
        var getValue= document.getElementById("a1");
        if (getValue.value !="") {
            getValue.value = "";
        }
        var getValue= document.getElementById("a2");
        if (getValue.value !="") {
            getValue.value = "";
        }
        var getValue= document.getElementById("a3");
        if (getValue.value !="") {
            getValue.value = "";
        }
        var getValue= document.getElementById("b1");
        if (getValue.value !="") {
            getValue.value = "";
        }
        var getValue= document.getElementById("b2");
        if (getValue.value !="") {
            getValue.value = "";
        }
        var getValue= document.getElementById("b3");
        if (getValue.value !="") {
            getValue.value = "";
        }
        var getValue= document.getElementById("c1");
        if (getValue.value !="") {
            getValue.value = "";
        }
        var getValue= document.getElementById("c2");
        if (getValue.value !="") {
            getValue.value = "";
        }
        var getValue= document.getElementById("c3");
        if (getValue.value !="") {
            getValue.value = "";
        }


}