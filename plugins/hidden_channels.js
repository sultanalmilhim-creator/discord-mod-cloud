// FNNF Plugin: Show Hidden Channels
(function () {
    console.log("%c[FNNF] Show Hidden Channels Loaded", "color: #5262f2; font-weight: bold;");

    function patchHiddenChannels() {
        const styleId = "fnnf-hidden-channels-css";
        if (document.getElementById(styleId)) return;

        const style = document.createElement("style");
        style.id = styleId;
        style.innerText = `
            [class*="aria-hidden"] { display: flex !important; opacity: 0.6 !important; }
            [class*="channel"] [class*="locked"] { color: #f23f43 !important; }
        `;
        document.head.appendChild(style);
    }

    if (document.readyState === "complete") {
        patchHiddenChannels();
    } else {
        window.addEventListener("load", patchHiddenChannels);
    }
})();
