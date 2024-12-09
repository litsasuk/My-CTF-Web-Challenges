<?php
$SECRET  = `/readsecret`;
include "waf.php";
class User {
    public $role;
    function __construct($role) {
        $this->role = $role;
    }
}
class Admin{
    public $code;
    function __construct($code) {
        $this->code = $code;
    }
    function __destruct() {
        echo "Admin can play everything!";
        eval($this->code);
    }
}
function game($filename) {
    if (!empty($filename)) {
        if (waf($filename) && @copy($filename , "/tmp/tmp.tmp")) {
            echo "Well done!";
        } else {
            echo "Copy failed.";
        }
    } else {
        echo "User can play copy game.";
    }
}
function set_session(){
    global $SECRET;
    $data = serialize(new User("user"));
    $hmac = hash_hmac("sha256", $data, $SECRET);
    setcookie("session-data", sprintf("%s-----%s", $data, $hmac));
}
function check_session() {
    global $SECRET;
    $data = $_COOKIE["session-data"];
    list($data, $hmac) = explode("-----", $data, 2);
    if (!isset($data, $hmac) || !is_string($data) || !is_string($hmac) || !hash_equals(hash_hmac("sha256", $data, $SECRET), $hmac)) {
        die("hacker!");
    }
    $data = unserialize($data);
    if ( $data->role === "user" ){
        game($_GET["filename"]);
    }else if($data->role === "admin"){
        return new Admin($_GET['code']);
    }
    return 0;
}
if (!isset($_COOKIE["session-data"])) {
    set_session();
    highlight_file(__FILE__);
}else{
    highlight_file(__FILE__);
    check_session();
}
