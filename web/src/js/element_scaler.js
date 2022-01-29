document.addEventListener("DOMContentLoaded", (event) => {
    var everyElement = document.querySelectorAll("*") // 모든 요소 선택
    everyElement.forEach((item, index) => {
        if (item.hasAttribute("scale")) {
            item.style.transform += "scale({0})".format(item.getAttribute("scale"))
        }
    })
})