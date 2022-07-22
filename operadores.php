<?php

   $a = $_POST['num1'];
   $b = $_POST['num2'];
   $op= $_POST['operacao'];

   $a = $_POST['num1'];
   $b = $_POST['num2'];
   $op= $_POST['operacao'];

   if(!empty($op)) {
      if($op == '+')
         $c = $a + $b;
      elseif($op == '-')
         $c = $a - $b;
      elseif($op == '*')
         $c = $a*$b;
      else
         $c = $a/$b;

      echo "O resultado da operação: $c";

   }

?>