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

            const row = document.createElement("div");
            row.className = "download-row";

            const filename = document.createElement("span");
            filename.className = "filename";
            filename.textContent = file;

            const actions = document.createElement("div");
            actions.className = "actions";

            const download = document.createElement("a");
            download.className = "btn";
            download.href = BASE + "output/" + file;
            download.download = "";
            download.textContent = "📥 Download";

            const copy = document.createElement("button");
            copy.className = "btn";
            copy.textContent = "📋 Copy Link";

            copy.onclick = () => {

                const url =
                    window.location.origin +
                    BASE +
                    "output/" +
                    file;

                navigator.clipboard.writeText(url);

                showToast("Copied " + file);
            };

            actions.appendChild(download);
            actions.appendChild(copy);

            row.appendChild(filename);
            row.appendChild(actions);

            downloads.appendChild(row);
        }

    })
    .catch(error => {

        console.error(
            "Failed to load manifest:",
            error
        );

    });

function showToast(message) {

    const toast =
        document.getElementById("toast");

    toast.textContent = message;

    toast.classList.add("show");

    setTimeout(() => {

        toast.classList.remove("show");

    }, 1800);

}

function copyQuick(file) {

    const url =
        window.location.origin +
        BASE +
        "output/" +
        file;

    navigator.clipboard.writeText(url);

    showToast(file + " URL copied");

}