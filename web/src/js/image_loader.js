document.addEventListener("DOMContentLoaded", (event) => {
    function check_webp() {
        var elem = document.createElement('canvas');

        if (!!(elem.getContext && elem.getContext('2d'))) {
            return elem.toDataURL('image/webp').indexOf('data:image/webp') == 0;
        } else {
            return false;
        }
    }

    if (!check_webp()) {
        var everyElement = document.querySelectorAll("img, source") // 모든 이미지 선택
        everyElement.forEach((item, index) => {
            if (item.hasAttribute("src")) {
                item.setAttribute("src", item.getAttribute("src").replace(/\.webp$/, ".png"))
            }

            if (item.hasAttribute("srcset")) {
                item.setAttribute("srcset", item.getAttribute("srcset").replace(/\.webp$/, ".png"))
            }
        })
    }
})