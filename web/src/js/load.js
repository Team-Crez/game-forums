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

            var mapThumbnail = document.createElement("img")
            mapThumbnail.dataset.asyncSrc = "src/data/{0}/{1}".format(level, data[level].thumbnail)
            mapThumbnail.style.maxWidth = "100%"

            mapElem.appendChild(mapThumbnail)
            var artistElem = document.createElement("item")
            var artistInfo = document.createElement("info-tag"); artistInfo.innerText = "Artist"
            var musicElem = document.createElement("item")
            var musicInfo = document.createElement("info-tag"); musicInfo.innerText = "Music"
            var creatorElem = document.createElement("item")
            var creatorInfo = document.createElement("info-tag"); creatorInfo.innerText = "Creator"
            var diffElem = document.createElement("item")
            var diffInfo = document.createElement("info-tag"); diffInfo.innerText = "Difficulty"
            
            artistElem.appendChild(artistInfo)
            musicElem.appendChild(musicInfo)
            creatorElem.appendChild(creatorInfo)
            diffElem.appendChild(diffInfo)

            artistElem.append("{0}".format(data[level].artist))
            musicElem.append("{0}".format(data[level].music))
            creatorElem.append("{0}".format(data[level].creator))
            diffElem.append("{0}".format(data[level].difficulty))
            
            mapSection.appendChild(mapElem)
            mapThumbnail.addEventListener("load", (event) => {
                mapElem.classList.add("map-block")

                mapElem.appendChild(artistElem)
                mapElem.appendChild(musicElem)
                mapElem.appendChild(creatorElem)
                mapElem.appendChild(diffElem)
            })
        })
    }
})