let preset_color = document.querySelectorAll('.preset_color');
let r = document.querySelector(':root');

let add_todo_form_container = document.querySelector('.add-toDo');
if(add_todo_form_container) {
    add_todo_form_container.querySelector('.colors').firstElementChild.querySelector('.color_input').setAttribute('checked', 'checked');
}

preset_color.forEach(e => {
    let color_input = e.querySelector('.color_input')
    let task_color = "#" + color_input.getAttribute('id');
    if (color_input.hasAttribute("checked")) {
        r.style.setProperty('--task-color', task_color);
    }
    let label = e.querySelector('label');
    label.style.backgroundColor = task_color;
    label.addEventListener('click', () => {
        r.style.setProperty('--task-color', task_color);
    });
});

