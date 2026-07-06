fetch("../output/manifest.json")

.then(r=>r.json())

.then(m=>{

document.getElementById("stats").innerHTML=`

<p><b>Channels:</b> ${m.channels}</p>

<p><b>Programmes:</b> ${m.programmes}</p>

<p><b>Generated:</b> ${m.generated}</p>

`;

});