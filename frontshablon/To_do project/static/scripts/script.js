const body = document.querySelector("body"),
	sidebar = document.querySelector(".sidebar"),
	toggle = document.querySelector(".toggle-btn"),
	searchBtn = document.querySelector(".search-box"),
	modeSwitch = document.querySelector(".toggle-switch"),
	modeText = document.querySelector(".mode-text");


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
	return `${d.toLocaleString('en-us', { month: 'short' })} ${d.getDate()}, ${d.getFullYear()}`;
}

document.querySelector('.current-day_weekday').innerText = getWeekDay()
document.querySelector('.current-day_fullDate').innerText = getFullDate()



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
