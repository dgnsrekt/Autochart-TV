$(document).ready(function() {
    var elements = document.getElementsByClassName('tradingview');
    if (elements.length == 1) {
        document.getElementsByTagName('section')[0].style.height = '100%'
        document.getElementsByTagName('section')[0].style.width = '100%'
    }

    if (elements.length == 2) {
        document.getElementsByTagName('section')[1].style.height = '50%'
        document.getElementsByTagName('section')[1].style.width = '100%'

        document.getElementsByTagName('section')[0].style.height = '50%'
        document.getElementsByTagName('section')[0].style.width = '100%'
    }

    if (elements.length == 3) {
        document.getElementsByTagName('section')[2].style.height = '50%'
        document.getElementsByTagName('section')[2].style.width = '50%'

        document.getElementsByTagName('section')[1].style.height = '50%'
        document.getElementsByTagName('section')[1].style.width = '50%'

        document.getElementsByTagName('section')[0].style.height = '50%'
        document.getElementsByTagName('section')[0].style.width = '100%'

    }

    if (elements.length == 4) {
        document.getElementsByTagName('section')[3].style.height = '50%'
        document.getElementsByTagName('section')[3].style.width = '50%'

        document.getElementsByTagName('section')[2].style.height = '50%'
        document.getElementsByTagName('section')[2].style.width = '50%'

        document.getElementsByTagName('section')[1].style.height = '50%'
        document.getElementsByTagName('section')[1].style.width = '50%'

        document.getElementsByTagName('section')[0].style.height = '50%'
        document.getElementsByTagName('section')[0].style.width = '50%'

    }

    if (elements.length == 5) {
        document.getElementsByTagName('section')[4].style.height = '50%'
        document.getElementsByTagName('section')[4].style.width = '33.3%'

        document.getElementsByTagName('section')[3].style.height = '50%'
        document.getElementsByTagName('section')[3].style.width = '33.3%'

        document.getElementsByTagName('section')[2].style.height = '50%'
        document.getElementsByTagName('section')[2].style.width = '33.3%'

        document.getElementsByTagName('section')[1].style.height = '50%'
        document.getElementsByTagName('section')[1].style.width = '50%'

        document.getElementsByTagName('section')[0].style.height = '50%'
        document.getElementsByTagName('section')[0].style.width = '50%'

    }

    if (elements.length == 6) {
        document.getElementsByTagName('section')[5].style.height = '50%'
        document.getElementsByTagName('section')[5].style.width = '33.3%'

        document.getElementsByTagName('section')[4].style.height = '50%'
        document.getElementsByTagName('section')[4].style.width = '33.3%'

        document.getElementsByTagName('section')[3].style.height = '50%'
        document.getElementsByTagName('section')[3].style.width = '33.3%'

        document.getElementsByTagName('section')[2].style.height = '50%'
        document.getElementsByTagName('section')[2].style.width = '33.3%'

        document.getElementsByTagName('section')[1].style.height = '50%'
        document.getElementsByTagName('section')[1].style.width = '33.3%'

        document.getElementsByTagName('section')[0].style.height = '50%'
        document.getElementsByTagName('section')[0].style.width = '33.3%'

    }
    if (elements.length > 6) {
        var sections = document.getElementsByTagName('section');
        for(var i = 0; i < sections.length; i++){
            sections[i].style.width  = '33.3%';
            sections[i].style.height = '33.3%';
        }

    }

});
