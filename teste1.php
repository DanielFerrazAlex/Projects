<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Testes</title>
</head>
<body>
    <?php
        $preco = $_GET['p'];
        echo "O preço do produto é: R$ $preco".number_format($preco, 2);
        $preco += $preco*10/100;
        echo "O novo preço do produto é: R$ $preco".number_format($preco, 2);
    ?>
</body>
</html>