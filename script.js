const formLogin = document.querySelector('#login');
const formRegister = document.querySelector('#registration')

formRegister.addEventListener('submit', (event) => {
    event.preventDefault();
    const username = document.querySelector('#username').value;
    const email = document.querySelector('#email').value;
    const password = document.querySelector('#password').value;
    
    console.log(username,email,password);
    saveData(username, email, password);
});

function saveData(username, email, password) {
    fetch('http://127.0.0.1:5000/save_data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username, email, password })
    })
    .then(response => response.text())
    .then(message => alert(message))
    .catch(error => console.error(error));
  }


const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnLogin-popup')
const iconClose = document.querySelector('.icon-close')

registerLink.addEventListener('click', ()=> {
    wrapper.classList.add('active');

});

loginLink.addEventListener('click', ()=> {
    wrapper.classList.remove('active');

});

btnPopup.addEventListener('click', ()=> {
    wrapper.classList.add('active-popup');

});

iconClose.addEventListener('click', ()=> {
    wrapper.classList.remove('active-popup');

});

