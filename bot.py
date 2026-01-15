<!DOCTYPE html><html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Multi Tool Panel</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body{font-family:Arial;background:#0f172a;color:#fff;margin:0;padding:0}
    header{background:#020617;padding:15px;text-align:center;font-size:20px}
    .container{padding:20px}
    .card{background:#020617;border-radius:12px;padding:15px;margin-bottom:15px}
    input,button{width:100%;padding:12px;border-radius:8px;border:none;margin-top:10px}
    button{background:#2563eb;color:#fff;font-weight:bold;cursor:pointer}
    button:hover{background:#1d4ed8}
    pre{white-space:pre-wrap}
  </style>
</head>
<body>
<header>✨ Multi Utility Tool (HTML)</header>
<div class="container">  <div class="card">
    <h3>📊 SIM / CNIC Info</h3>
    <input id="number" placeholder="Enter Mobile or CNIC">
    <button onclick="fetchInfo()">Fetch Info</button>
    <pre id="result"></pre>
  </div>  <div class="card">
    <h3>🎬 TikTok Downloader</h3>
    <input id="tiktok" placeholder="Paste TikTok URL">
    <button onclick="downloadTikTok()">Get Video</button>
    <pre id="tt"></pre>
  </div>  <div class="card">
    <h3>📧 Temp Mail</h3>
    <button onclick="createMail()">Generate Email</button>
    <pre id="mail"></pre>
  </div></div><script>
const SIM_API = "https://fam-official.serv00.net/api/database.php?number=";
const TEMP_API = "https://temp-mail-fak.jokerkeep057.workers.dev/?key=32563";

function fetchInfo(){
  const num = document.getElementById('number').value;
  fetch(SIM_API + num)
    .then(r=>r.json())
    .then(d=>{
      let out='';
      for(let k in d){out+=k+": "+d[k]+"\n"}
      document.getElementById('result').innerText=out;
    })
    .catch(()=>alert('Error'));
}

function downloadTikTok(){
  const url=document.getElementById('tiktok').value;
  fetch(`https://mrking-tiktok-download-api.deno.dev/?url=${url}`)
    .then(r=>r.json())
    .then(d=>{
      document.getElementById('tt').innerHTML=`<a href="${d.video}" target="_blank">Download Video</a>`;
    })
}

function createMail(){
  fetch(TEMP_API+"&action=generate")
    .then(r=>r.json())
    .then(d=>{
      document.getElementById('mail').innerText=`Email: ${d.emailAddress}`;
    })
}
</script></body>
</html>
