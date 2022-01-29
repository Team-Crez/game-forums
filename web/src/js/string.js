String.prototype.format = function() {
    var formatted = this;
    Array.from(arguments).forEach((item, index) => {
        var regexp = new RegExp('\\{' + index + '\\}', 'gi')
        formatted = formatted.replace(regexp, item)
    })
    return formatted
}