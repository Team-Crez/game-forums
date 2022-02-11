var loadImageAsync = null

document.addEventListener("DOMContentLoaded", (event) => {

    function checkWebP() {
        var elem = document.createElement('canvas');

        if (!!(elem.getContext && elem.getContext('2d'))) {
            return elem.toDataURL('image/webp').indexOf('data:image/webp') == 0;
        } else {
            return false;
        }
    }

    function convertSrc(src, isSupportWebP) {
        if (isSupportWebP) {
            return src
        } else {
            return src.replace(/\.webp$/, ".png")
        }
    }

    isSupportWebP = checkWebP()

    var everyElement = document.querySelectorAll("source, img") // 모든 이미지 선택
    everyElement.forEach((item, index) => {
        if (item.hasAttribute("data-src")) {
            var finalSrc = convertSrc(item.dataset.src, isSupportWebP)
            switch (item.tagName.toLowerCase()) {
                case "img":
                    item.setAttribute("src", finalSrc)
                    break
                
                case "source":
                    item.setAttribute("srcset", finalSrc)
                    break
            }
        }
    })

    var processElement = (mutationsList, observer) => {
        imageTags = ["source", "img"]
        mutationsList.forEach(mutation => {
            imgItems = mutation.target.querySelectorAll("source, img")
            imgItems.forEach(item => {
                if (!(item.hasAttribute("src") || item.hasAttribute("srcset"))) {
                    if (item.hasAttribute("data-src")) {
                        var finalSrc = convertSrc(item.dataset.src, isSupportWebP)
                        switch (item.tagName.toLowerCase()) {
                            case "img":
                                item.setAttribute("src", finalSrc)
                                break
                            
                            case "source":
                                item.setAttribute("srcset", finalSrc)
                                break
                        }
                    }

                    loadImageAsync(item)
                }
            })
            
        })
    }

    loadImageAsync = (item) => {
        if (item.hasAttribute("data-async-src")) {
            item.setAttribute("decoding", "async")
            var finalSrc = convertSrc(item.dataset.asyncSrc, isSupportWebP)
            switch (item.tagName.toLowerCase()) {
                case "img":
                    item.setAttribute("src", finalSrc)
                    break
                
                case "source":
                    item.setAttribute("srcset", finalSrc)
                    break
            }
        }
    }

    const observer = new MutationObserver(processElement)
    observer.observe(document.body, { attributes: true, childList: true, subtree: true })
})