<?php
$encrypted_text=$_GET['text'];
$file = fopen("storagefile.txt","w");
fwrite($file,$encrypted_text);
fclose($file);
echo("Success");
?>