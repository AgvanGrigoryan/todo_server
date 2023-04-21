let preset_color = document.querySelectorAll('.preset_color');
				let r = document.querySelector(':root');

				const edit_btn = document.querySelectorAll('.edit_toggle_btn')
				edit_btn.forEach(el => {
					el.addEventListener('click', (e)=>{
						el.closest('.flip-card').classList.toggle('flipped');
					})
				});


					if (preset_color.length > 0) {
						preset_color.forEach(e => {
							let color_input = e.querySelector('.color_input')
							let task_color = "#" + color_input.getAttribute('value');
							if (color_input.hasAttribute("checked")) {
								r.style.setProperty('--task-color', task_color);
							}
							let label =e.querySelector('label');
							label.style.backgroundColor = task_color;
							label.addEventListener('click', (e) => {
								r.style.setProperty('--task-color', task_color);
							});
						});
					}