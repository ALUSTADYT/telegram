<?php
header("Content-Type: application/json");
header("Access-Control-Allow-Origin: *");

if(!isset($_GET['url']) || empty($_GET['url'])){
    echo json_encode(["status"=>false,"msg"=>"No URL"]);
    exit;
}

$url = urlencode($_GET['url']);
$api = "https://api.instadownloader.org/api/download?url=".$url;

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $api);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/5.0");

$response = curl_exec($ch);
curl_close($ch);

echo $response;
