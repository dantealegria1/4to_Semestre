function datos()
{
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var data = JSON.parse(this.responseText);
            var mayores30 = 0;
            var mujeres = 0;
            var hombres = 0;
            var menores25 = 0;
            var Joe = 0;
            var Moe = 0;
            var Kim = 0;
            
            for (var i = 0; i < data.length; i++) {
                if(data[i].edad > 29 && data[i].sex == "H")
                {
                    mayores30 = mayores30 + 1;  
                }
                if(data[i].edad < 26 && data[i].sex == "M")
                {
                    menores25 = menores25 + 1;
                }
                if(data[i].sex == "M")
                {
                    mujeres = mujeres + 1;
                }else
                {
                    hombres = hombres + 1;
                }
                if(data[i].nom == "Joe")
                {
                    Joe = Joe + 1;
                }else if(data[i].nom == "Moe")
                {
                    Moe = Moe + 1;
                }else if(data[i].nom == "Kim" && data[i].edad > 26)
                {
                    Kim = Kim + 1;
                }
            }

            document.getElementById("Mayores30").innerHTML = mayores30+ " Hombres";
            document.getElementById("Mujeres").innerHTML = mujeres+ " Mujeres";
            document.getElementById("Hombres").innerHTML = hombres+ " Hombres";
            document.getElementById("Menores25").innerHTML = menores25+ " Mujeres";
            document.getElementById("Joe").innerHTML = Joe+ " Hombres";
            document.getElementById("Moe").innerHTML = Moe+ " Hombres";
            document.getElementById("Kim").innerHTML = Kim+ " Mujeres";
        }
    };
    xmlhttp.open("GET", "arhivo.json", true);
    xmlhttp.send();
}