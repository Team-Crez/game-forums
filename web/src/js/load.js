var mapData = null;

document.addEventListener("DOMContentLoaded", (event) => {
    fetch("src/data/levels.json", {
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
        
        Object.keys(data).forEach((level) => {
            var mapElem = document.createElement("div")
            mapElem.classList.add("map-block")

            var mapThumbnail = document.createElement("img")
            mapThumbnail.dataset.src = "src/data/{0}/{1}".format(level, data[level].thumbnail)
            mapThumbnail.style.maxWidth = "100%"

            mapElem.appendChild(mapThumbnail)
            var artistElem = document.createElement("item")
            var artistInfo = document.createElement("info-tag"); artistInfo.innerText = "Artist"
            var musicElem = document.createElement("item")
            var musicInfo = document.createElement("info-tag"); musicInfo.innerText = "Music"
            
            artistElem.appendChild(artistInfo)
            musicElem.appendChild(musicInfo)

            artistElem.append("{0}".format(data[level].artist))
            musicElem.append("{0}".format(data[level].music))

            mapElem.appendChild(artistElem)
            mapElem.appendChild(musicElem)
            
            mapSection.appendChild(mapElem)
        })
    }
})