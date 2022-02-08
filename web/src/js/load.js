var mapData = null;

document.addEventListener("DOMContentLoaded", (event) => {
    fetch("src/maps/maps.json", {
        method: 'get',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then((response) => {
        return response.json()
    }).then((result) => {
        showMaps(result)
    }).catch((err) => console.log(err))

    function showMaps(data) {
        var mapSection = document.querySelector(".maps")
        var mapElem = document.createElement("div")
        mapElem.classList.add("map-block")
        mapElem.innerText = Object.keys(data)[0]

        // mapSection.appendChild(mapElem)
    }
})