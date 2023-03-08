async function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function getCookie(name) {
    const value = "; " + document.cookie;
    const parts = value.split("; " + name + "=");
    if (parts.length === 2) return parts.pop().split(";").shift();
}

function set_input_value_by_id(input_id, value) {
    document.getElementById(input_id).value = value;
}

const themeChangeBtns = document.getElementsByClassName('theme-change-btn');
for (let i = 0; i < themeChangeBtns.length; i++) {
    themeChangeBtns[i].addEventListener('click', function () {
        const curId = parseInt(bgImage.getAttribute('themeId'));
        const maxId = 2;
        let forSetId = curId + 1;
        if (forSetId > maxId) {
            forSetId = 1;
        }
        setThemeById(forSetId);
    })
}
window.onload = function (e) {
    document.getElementById('loading_spinner_block').remove();
    document.getElementById('content').classList.remove('d-none');
    let telegram_auth = document.getElementById('telegram-login-xlartas_web_bot')
    if (telegram_auth) {
        telegram_auth.classList.add('telegram-auth');
    }
}