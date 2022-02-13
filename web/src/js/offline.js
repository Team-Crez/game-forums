if ('serviceWorker' in navigator) {
    window.addEventListener("load", () => {
        navigator.serviceWorker
            .register("/service_worker.js")
            .then(res => console.log("registered"))
            .catch(err => console.log(err))
    })
}