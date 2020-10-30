<!-- 

<?php

if (isset($_POST["lessons"])){
    $var=$_POST["lessons"];
}
else{
    $var=array("TONY","STEVE","JEFF","FRANKLIN");
    // (
    //     array("Volvo",22,18),
    //     array("BMW",15,13),
    //     array("Saab",5,2),
    //     array("Land Rover",17,15)
    // );
}


$var3=6;
$var2="<html>
<head></head>
<body><h1>HELOOW</h1>
<form action='http://localhost/lesson/index.php' method = 'POST'>
<input type='text' name='name'>Your Name</input> <br />
<b>What lesson do you learn?</b><br>
<select name = 'lessons[]' size='4' multiple>
    <option value='mysql'>My SQL</option>
    <option value='web_dev'>Web Dev</option>
    <option value='oracle'>Oracle</option>
    <option value='javascript'>Javascript</option>
</select>
<input type = 'submit' value='Submit'>
</form> </body>
</html>";

// array_push($var, "BILLT");
// array_pop($var);
// $var[2]="Arnold";

foreach($var as $index)
{
    echo $index." ";
    echo "<br>";
}

// foreach($var as $index){
//     echo $index;
//     echo "<br>";

// }

// print_r($var);
echo $var2;

?> -->

<?php
$mysqli=new mysqli("localhost","demo","9ToW1d1ZPGfYBbRg", "person");

$result=$mysqli->query("select first_name from name");

dbquery($result);




function dbquery($result){
    while($row=$result->fetch_array()){
        echo $row['first_name']." ";
    }

}
?>