function validar() {
    
    var Correo = document.getElementById("Correo").value;
    var Contraseña = document.getElementById("Contraseña").value;
    contador = 0

    if (Correo == "") 
    {
        alert("El campo Correo esta vacio");
        return false;
    }
    if (Contraseña == "") 
    {
        alert("El campo Contraseña esta vacio");
        return false;
    }

    for(i=0; i<Correo.length; i++)
    {
        if(Correo.charAt(i) == "@")
        {
            contador = contador + 1
        }
    }

    if(contador == 0)
    {
        alert("El correo no tiene el @");
        return false;
    }

    if(contador > 1)
    {
        alert("El correo tiene mas de un @");
        return false;
    }

    if(Contraseña.length < 8)
    {
        alert("La contraseña es muy corta");
        return false;
    }

    alert("Bienvenido");
    return true;
}