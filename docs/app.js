const BASE = "/runn-tv-epg/";

fetch(BASE + "output/manifest.json")
    .then(response => response.json())
    .then(manifest => {

        document.getElementById("channels").textContent =
            manifest.channels;

        document.getElementById("programmes").textContent =
            manifest.programmes;

        document.getElementById("updated").textContent =
            new Date(manifest.generated).toLocaleString();


        const downloads =
            document.getElementById("downloads");


        for (const [name, file] of Object.entries(manifest.downloads)) {

            const link = document.createElement("a");

            link.className = "download";

            link.href = BASE + "output/" + file;

            link.textContent = "📥 " + file;

            downloads.appendChild(link);
        }

    })
    .catch(error => {

        console.error(
            "Failed to load manifest:",
            error
        );

    });