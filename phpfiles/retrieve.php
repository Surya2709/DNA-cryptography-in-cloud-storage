<?php

$data=file_get_contents("storagefile.txt","r");
$array=array('data'=>$data);

echo json_encode($array);

?>
