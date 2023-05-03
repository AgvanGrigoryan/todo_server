const signupButton = document.getElementById('signup-button'),
    loginButton = document.getElementById('login-button'),
    userForms = document.getElementById('user_options-forms');


/**
 * Add event listener to the "Sign Up" button
 */
signupButton.addEventListener('click', () => {
    userForms.classList.remove('bounceRight')
    // if (userForms.classList.contains('signup')) {
    userForms.classList.add('signup')

    // }
    userForms.classList.add('bounceLeft')
}, false)

/**
 * Add event listener to the "Login" button
 */
loginButton.addEventListener('click', () => {
    userForms.classList.remove('signup')

    userForms.classList.remove('bounceLeft')
    userForms.classList.add('bounceRight')
}, false);

//Form Validator
class FormValidator {
    constructor(form, fields) {
        this.form = form
        this.fields = fields
        this.isValid = {}
        this.fields.forEach(field => {
            this.isValid[field] = false
        })
    }

    initialize() {
        this.validateOnEntry()
        // this.validateOnSubmit()
        // this.formChanged()
    }

    validateOnSubmit() {
        let self = this

        this.form.addEventListener('submit', e => {
            e.preventDefault()
            self.fields.forEach(field => {
                const input = document.querySelector(`#${field}`)
                self.validateFields(input)
            })
        })
        console.log(Object.values(this.isValid))
    }

    validateOnEntry() {
        let self = this
        this.fields.forEach(field => {
            const input = document.querySelector(`#${field}`)

            input.addEventListener('input', event => {
                self.validateFields(input)
                this.isAllValid()
            })
        })
    }

    isAllValid() {
        let submitBtn = this.form.querySelector('.forms_buttons-action')
        let isFormValid = true;
        Object.values(this.isValid).forEach(val => {
            if (val === false) {
                submitBtn.setAttribute('disabled', 'disabled')
                isFormValid = false;
            }
        })
        if (isFormValid) {
            submitBtn.removeAttribute('disabled')
        }
    }


    validateFields(field) {
        // Check presence of values
        if (field.value.trim() === "") {
            this.setStatus(field, `${field.getAttribute('placeholder')} cannot be blank`, "error")
        } else {
            this.setStatus(field, null, "success")
        }

        // Check for a valid username field
        if (field.id === "reg_username") {
            const re = /^[a-zA-Z0-9]+$/;
            if (re.test(String(field.value).toLowerCase())) {
                this.IsFree(this.form, 'http://127.0.0.1:8000/user/signup/isUsernameFree/', field, 'This username is already taken')
            } else {
                this.setStatus(field, "Please enter valid username", "error")
            }
        }

        // check for a valid email address
        if (field.type === "email") {
            const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            if (re.test(String(field.value).toLowerCase())) {
                this.IsFree(this.form, 'http://127.0.0.1:8000/user/signup/isEmailFree/', field, 'This email is already taken')
            } else {
                this.setStatus(field, "Please enter valid email address", "error")
            }
        }

        //Passwords match check
        if (field.id === "id_password1") {
            const confirmPasswordField = this.form.querySelector('#id_password2')

            if (field.value !== confirmPasswordField.value) {
                this.setStatus(field, "Password does not match", "error")
            } else {
                this.setStatus(field, null, "success")
                this.setStatus(confirmPasswordField, null, "success")
            }
        }

        // Password confirmation edge case
        if (field.id === "id_password2") {
            const passwordField = this.form.querySelector('#id_password1')

            if (field.value.trim() === "") {
                this.setStatus(field, "Password confirmation required", "error")
            } else if (field.value !== passwordField.value) {
                this.setStatus(field, "Password does not match", "error")
            } else {
                this.setStatus(field, null, "success")
                this.setStatus(passwordField, null, "success")
            }
        }

    }

    setStatus(field, message, status) {
        let errorMessage = field.parentElement.querySelector('.inp_error-message');

        if (status === "success") {
            this.isValid[field.id] = true
            if (errorMessage) {
                errorMessage.innerText = ""
            }
            field.classList.remove('input-error')
        }

        if (status === "error") {
            this.isValid[field.id] = false
            errorMessage.innerText = message
            errorMessage.style.color = 'darkred'
            field.classList.add('input-error')
        }
    }

    IsFree(form, action, input, error_message) {
        let data = {};
        let inputName = input.name;
        data[inputName] = input.value;
        try {
            fetch(`${action}`, {
                headers: {
                    "Content-Type": 'application/x-www-form-urlencoded',
                    "X-CSRFToken": form['csrfmiddlewaretoken'].value,
                },
                method: "POST",
                body: JSON.stringify(data)
            }).then(response => {
                response.json().then((data) => {
                    if (data.status === 'busy') {
                        this.setStatus(input, error_message, "error")
                        this.isValid[input.id] = false
                        console.log(`error ${inputName}`)
                    } else if (data.status === 'free') {
                        this.setStatus(input, null, "success")
                        this.isValid[input.id] = true
                        console.log(`success ${inputName}`)
                    }
                })
            });
        } catch (err) {
            console.log(err)
        }
    }

}

const reg_form = document.querySelector('#registration_form')
const fields = ["id_first_name", "reg_username", "id_email", "id_password1", "id_password2"]

const validator = new FormValidator(reg_form, fields)
validator.initialize()