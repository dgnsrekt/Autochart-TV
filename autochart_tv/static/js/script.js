$(document).ready(function() {
    var elements = document.getElementsByClassName('tradingview');
    if (elements.length <= 1) {
        console.log('less than 1')
        document.getElementsByTagName('section')[0].style.height = '100%'
        document.getElementsByTagName('section')[1].style.width = '100%'
    }

    if (elements.length > 1) {
        console.log('more than 1')
        document.getElementsByTagName('section')[0].style.height = '50%'
        document.getElementsByTagName('section')[0].style.width = '100%'

        document.getElementsByTagName('section')[1].style.height = '50%'
        document.getElementsByTagName('section')[1].style.width = '100%'
    }
});