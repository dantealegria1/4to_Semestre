function suma()
{
    var s1 = document.getElementById('num1').value;
    var s2 = document.getElementById('num2').value;
    var tot = parseInt(s1) + parseInt(s2);
    document.getElementById('resultado').value = tot;

}