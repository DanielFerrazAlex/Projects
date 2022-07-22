<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        $ano = 2022;
        echo "O ano atual é $ano e ano passado foi ".--$ano;
        echo "<br/>O ano que vem é ".$ano+=2;
    ?>
</body>
</html>