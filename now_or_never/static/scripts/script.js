const body = document.querySelector("body"),
    sidebar = document.querySelector(".sidebar"),
    toggle = document.querySelector(".toggle-btn"),
    searchBtn = document.querySelector(".search-box"),
    modeSwitch = document.querySelector(".toggle-switch"),
    modeText = document.querySelector(".mode-text"),
    isdoneForms = document.querySelectorAll(".todo_isdone_form"),
    isdoneChechboxes = document.querySelectorAll(".todo_isdone_checkbox");

//actions menu toggle
let button = document.querySelector('.action__menu-btn');
if (button) {
    button.addEventListener('click', () => {
        let menu = button.nextElementSibling;
        menu.classList.toggle('closed');
    });
}


if (localStorage.getItem('theme') === "dark") {
    body.classList.add("dark");
    if (modeText) {
        modeText.innerText = "Dark Mode"
    }


} else {
    body.classList.remove("dark");
    modeText.innerText = "Light Mode"


}
if (localStorage.getItem("sidebar-status") === "closed") {
    body.classList.add("sidebar-close")
} else {
    body.classList.remove("sidebar-close")

}


function getWeekDay() {
    let d = new Date();
    var weekDays = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
    ];
    return weekDays[d.getDay()];

}

function getFullDate() {
    let d = new Date();
    return `${d.toLocaleString('en-us', {month: 'short'})} ${d.getDate()}, ${d.getFullYear()}`;
}

const curWeekday = document.querySelector('.current-day_weekday')
const curFullDate = document.querySelector('.current-day_fullDate')
if (curWeekday != null && curFullDate != null) {
    curWeekday.innerText = getWeekDay();
    curFullDate.innerText = getFullDate();
}

if (toggle) {
    toggle.addEventListener('click', () => {
        body.classList.toggle("sidebar-close");
        if (body.classList.contains("sidebar-close")) {
            localStorage.setItem("sidebar-status", "closed")
        } else {
            localStorage.setItem("sidebar-status", "opened")

        }
    });
}

if (modeSwitch) {
    modeSwitch.addEventListener('click', () => {
        body.classList.toggle("dark");
        if (body.classList.contains("dark")) {
            modeText.innerText = "Dark Mode"
            localStorage.setItem('theme', 'dark')

        } else {
            modeText.innerText = "Light Mode";
            localStorage.setItem('theme', 'light');

        }
    });
}

/*A lot of updates requests blocker on Main Page*/
let locked = false;
let requestCount = 0
if (0 < localStorage.getItem('blockedSeconds') && localStorage.getItem('blockedSeconds') !== null) {
    lockrequest(localStorage.getItem('blockedSeconds'))
} else {
    if (isNaN(localStorage.getItem('NextblockSeconds')) || localStorage.getItem('NextblockSeconds') === null) {
        localStorage.setItem('NextblockSeconds', 5)
    }
}

//Requests counter
isdoneForms.forEach((e) => {
    e.addEventListener('change', () => {
        if (requestCount === 0) {
            setTimeout(() => {
                if (requestCount >= 8) {
                    lockrequest(localStorage.getItem('NextblockSeconds'))
                } else {
                    requestCount = 0
                }
            }, 2000);
        }
        if (locked === false) {
            isDoneUpdate(e);
            requestCount += 1;
        }
    })
})

//Request Lock Timer
function lockrequest(sec) {
    locked = true;
    isdoneChechboxes.forEach(inp => {
        inp.setAttribute('disabled', 'disabled');
    })
    alert(`Очень много запросов за единицу времени, ${sec} секунд до разблокировки`);
    let blockInterval = setInterval(() => {
        if (sec <= 0) {
            let localNextBlockSec = +localStorage.getItem('NextblockSeconds');
            localStorage.setItem('NextblockSeconds', Math.ceil(localNextBlockSec * Math.log(localNextBlockSec)));
            localStorage.setItem('blockedSeconds', 0);
            locked = false;
            requestCount = 0;
            isdoneChechboxes.forEach(inp => {
                inp.removeAttribute('disabled');
            });
            clearInterval(blockInterval)

        } else {
            sec -= 1;
            localStorage.setItem('blockedSeconds', sec);
        }
    }, 1000);
}

//Send request to Update isDone status
function isDoneUpdate(form) {
    fetch(`${form.action}`, {
        headers: {
            "Content-Type": 'application/x-www-form-urlencoded',
            "X-CSRFToken": form['csrfmiddlewaretoken'].value,

        },
        method: "POST",
        body: JSON.stringify({'is_done': form['is_done'].checked.toString()})
    }).catch(error => alert("Ошибка"));
}

function ajaxSend(url, params) {
    fetch(`${url}?${params}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencocded',
        },
    })
        .then(response => response.json())
        .then(json => render(json))
        .catch(error => console.error(error));
}


//Show Error,Warning,Success Messages
let error_container = document.querySelector('.messages_container');
if (error_container) {
    let errors = error_container.querySelector('.errors');
    error_container.classList.add('active');
    close_errorTimer = setTimeout(function () {
        error_container.classList.remove('active');
    }, 8000);
    error_container.addEventListener('click', function () {
        clearTimeout(close_errorTimer);
        error_container.classList.remove('active');

    });
}

let image_input = document.querySelector('#id_image');
image_input.addEventListener('change', previewFile);

function previewFile() {
    let img_demo = document.querySelector('.user_image_demo');
    let file = image_input.files[0];
    var reader = new FileReader();

    reader.onloadend = function () {
        img_demo.src = reader.result;
    }

    if (file) {
        reader.readAsDataURL(file);
    } else {
        img_demo.src = "";
    }
}