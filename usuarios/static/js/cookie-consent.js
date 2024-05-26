document.addEventListener("DOMContentLoaded", function() {
    const cookieConsent = document.getElementById('cookie-consent');
    const acceptCookiesButton = document.getElementById('accept-cookies');

    if (getCookie('cookies_accepted') !== 'true') {
        cookieConsent.style.display = 'block';
    }

    acceptCookiesButton.addEventListener('click', function() {
        fetch('/accept-cookies/')
            .then(response => response.json())
            .then(data => {
                if (data.status === 'ok') {
                    cookieConsent.style.display = 'none';
                }
            });
    });

    function getCookie(name) {
        let cookieArr = document.cookie.split(";");
        for (let i = 0; i < cookieArr.length; i++) {
            let cookiePair = cookieArr[i].split("=");
            if (name == cookiePair[0].trim()) {
                return decodeURIComponent(cookiePair[1]);
            }
        }
        return null;
    }
});