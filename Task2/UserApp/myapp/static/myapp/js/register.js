const username_input = document.getElementById('username')
let username_isvalid = false
username_input.addEventListener('input', event => {
  if (event.target.value) {
    fetch('/user/hgfjhjdgUserList/')
      .then(function (response) {
        return response.json()
      })
      .then(function (json) {
        const res = json.data.filter(
          username => username === event.target.value.trim()
        )
        if (res.length > 0) {
          event.target.classList.add('invalid-input')
          const helper = document.getElementById('username-helper')
          helper.classList.add('help-bad')
          helper.textContent = 'User Name Already Exists'
          username_isvalid = false
        } else {
          event.target.classList.remove('invalid-input')
          const helper = document.getElementById('username-helper')
          helper.classList.add('help-ok')
          helper.textContent = ''
          username_isvalid = true
        }
      })
  }
})

const password_input = document.getElementById('password')
let pass_isvalid = false
password_input.addEventListener('input', event => {
  const pass = event.target.value
  const pass_helper = document.getElementById('password-helper')
  const getHTML = text => `<li>${text}</li>`
  const errList = []
  if (pass.length < 6) {
    errList.push('The Password Should be min of 6 characters')
  }
  if (pass.search(/[0-9]/) < 0) {
    errList.push('Your password must contain at least one digit.')
  }
  if (pass.search(/[!@#$%^&*_]/) < 0) {
    errList.push('Your password must contain at least one special character.')
  }

  pass_helper.innerHTML = errList.map(err => getHTML(err)).join('')
  if (errList.length > 0) {
    pass_isvalid = false
    event.target.classList.add('invalid-input')
  } else {
    pass_isvalid = true
    event.target.classList.remove('invalid-input')
  }
})

const cpassword_input = document.getElementById('confirm-password')
let cpass_isvalid = false
cpassword_input.addEventListener('input', event => {
  if (event.target.value !== password_input.value) {
    const cpass_help = document.getElementById('cpassword-helper')
    cpass_help.textContent = 'The passwords does not match'
    cpass_isvalid = false
    event.target.classList.add('invalid-input')
  } else {
    const cpass_help = document.getElementById('cpassword-helper')
    cpass_help.textContent = ''
    cpass_isvalid = true
    event.target.classList.remove('invalid-input')
  }
})

const form = document.getElementById('register-form')
form.addEventListener('submit', event => {
  if (!(username_isvalid && pass_isvalid && cpass_isvalid)) {
    alert('The form is Invalid')
  }
})
