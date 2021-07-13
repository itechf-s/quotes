let isNotLoad = true;

function setImage() {
    if(isNotLoad) {
        console.log('setImage');
        var imgEl = document.getElementsByTagName('img');
        for (var m=0; m<imgEl.length; m++) {
        if(imgEl[m].getAttribute('data-src')) {
        imgEl[m].setAttribute('src',imgEl[m].getAttribute('data-src'));
        imgEl[m].removeAttribute('data-src');
            }
        }
        isNotLoad = false;
    }
}

document.addEventListener("scroll", setImage);
window.addEventListener("resize", setImage);
window.addEventListener("orientationChange", setImage);