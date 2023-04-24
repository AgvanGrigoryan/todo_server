const body = document.querySelector("body"),
    sidebar = document.querySelector(".sidebar"),
    toggle = document.querySelector(".toggle-btn"),
    searchBtn = document.querySelector(".search-box"),
    modeSwitch = document.querySelector(".toggle-switch"),
    modeText = document.querySelector(".mode-text"),
    isdoneForm = document.querySelectorAll(".todo_isdone_form"),
    isdoneChechbox = document.querySelectorAll(".todo_isdone_checkbox");


if (localStorage.getItem('theme') === "dark") {
    body.classList.add("dark");
    modeText.innerText = "Dark Mode"


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
if (curWeekday != null && curFullDate != null){
    curWeekday.innerText = getWeekDay();
    curFullDate.innerText = getFullDate();
}


toggle.addEventListener('click', () => {
    body.classList.toggle("sidebar-close");
    if (body.classList.contains("sidebar-close")) {
        localStorage.setItem("sidebar-status", "closed")
    } else {
        localStorage.setItem("sidebar-status", "opened")

    }
});

modeSwitch.addEventListener('click', () => {
    body.classList.toggle("dark");
    if (body.classList.contains("dark")) {
        modeText.innerText = "Dark Mode"
        localStorage.setItem('theme', 'dark')

    } else {
        modeText.innerText = "Light Mode"
        localStorage.setItem('theme', 'light')

    }
});

isdoneForm.forEach((e) => {
    e.addEventListener('change', () => {
        console.log(e['is_done'].checked)
        fetch(`${e.action}`, {
            headers: {
                "Content-Type": 'application/x-www-form-urlencoded',
                "X-CSRFToken": e['csrfmiddlewaretoken'].value,

            },
            method: "POST",
            body: JSON.stringify({'is_done': e['is_done'].checked.toString()})
        }).catch(error => alert("Ошибка"));
    })
})

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

