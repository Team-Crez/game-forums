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
            mapThumbnail.classList.add("thumbnail")

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
            diffElem.append("{0}".format(data[level].difficulty.toFixed(2)))
            
            mapSection.appendChild(mapElem)
            mapThumbnail.addEventListener("load", (event) => {
                mapElem.classList.add("map-block")
                mapThumbnail.style.maxWidth = "100%"

                mapElem.appendChild(artistElem)
                mapElem.appendChild(musicElem)
                mapElem.appendChild(creatorElem)
                mapElem.appendChild(diffElem)
            })
        })
    }

    try {
        if (new RegExp("; en-US; Valve Steam Tenfoot\\/[0-9]*; \\)").test(navigator.userAgent)) {
            var infoTag = document.createElement("info-tag"); infoTag.innerText = "Steam에서 이용하고 계시네요!"
            
            infoTag.classList.add("display-block")
            infoTag.classList.add("center")
            infoTag.style.marginTop = "2.8vh"

            document.body.insertBefore(infoTag, document.body.children[1])
        }
    } catch (error) {
        document.write(error)
    }
})