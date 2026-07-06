fetch("../output/manifest.json")

.then(r => r.json())

.then(m => {

document.getElementById("channels").textContent =
m.channels;

document.getElementById("programmes").textContent =
m.programmes;

document.getElementById("updated").textContent =
new Date(m.generated).toLocaleString();

const downloads =
document.getElementById("downloads");

for(const [name,file] of Object.entries(m.downloads)){

const a=document.createElement("a");

a.className="download";

a.href="../output/"+file;

a.textContent="📥 "+file;

downloads.appendChild(a);

}

});