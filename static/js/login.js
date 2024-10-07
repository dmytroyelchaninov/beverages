document.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.getElementById('registerForm');
    const loginForm = document.getElementById('loginForm');
    const toggleToRegister = document.getElementById('toggleToRegister');
    const toggleToLogin = document.getElementById('toggleToLogin');
    const loginWrapper = document.querySelector('.login-wrapper');
    const registerWrapper = document.querySelector('.register-wrapper');
    const pleaseConfirm = document.getElementById('pleaseConfirm');
    const invalidCredentials = document.getElementById('invalidCredentials');
    const errorGeneral = document.getElementById('errorGeneral');
    const loginButton = document.getElementById('loginButton');
    const loginButtonMobile = document.getElementById('loginButtonMobile');
    const headerMenu = document.querySelector('.header__menu');
    const wrapper = document.querySelector('.wrapper');
    const body = document.querySelector('body');

    loginButton.addEventListener('click', (e) => {
        e.preventDefault();
        body.classList.add('lock');
        wrapper.classList.add('blurred');
        loginWrapper.classList.add('active');
        // registerWrapper.classList.add('active');
    });

    loginWrapper.addEventListener('click', (e) => {
        if (e.target == loginWrapper) {
            wrapper.classList.remove('blurred');
            loginWrapper.classList.remove('active');
            registerWrapper.classList.remove('active');
            body.classList.remove('lock');
        }
    });

    registerWrapper.addEventListener('click', (e) => {
        if (e.target == registerWrapper) {
            wrapper.classList.remove('blurred');
            registerWrapper.classList.remove('active');
            loginWrapper.classList.remove('active');
            body.classList.remove('lock');
        }
    });

    loginButtonMobile.addEventListener('click', (e) => {
        e.preventDefault();
        body.classList.add('lock');
        wrapper.classList.add('blurred');
        headerMenu.classList.remove('active');
        loginWrapper.classList.add('active');
    });

    toggleToRegister.addEventListener('click', (e) => {
        e.preventDefault();
        toggleForms('register');
    });

    toggleToLogin.addEventListener('click', (e) => {
        e.preventDefault();
        toggleForms('login');
    });

    function toggleForms(formType) {
        if (formType === 'register') {
            loginWrapper.classList.remove('active');
            registerWrapper.classList.add('active');
        } else {
            loginWrapper.classList.add('active');
            registerWrapper.classList.remove('active');
        }
    }

    function sendAjaxRequest(url, method, formData, successHandler, errorHandler) {
        $.ajax({
            url: url,
            type: method,
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: successHandler,
            error: errorHandler
        });
    }

    registerForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const formData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            password: document.getElementById('password').value,
            phone_number: document.getElementById('phone_number').value
        };

        sendAjaxRequest('/api/users/register', 'POST', formData, 
            function(data) {
                if (data.message === 'User created successfully') {
                    window.location.href = '/login.html';
                } else {
                    errorGeneral.style.display = 'block';
                }
            },
            function(error) {
                alert(error.responseJSON.message || 'Something went wrong, please contact us');
            }
        );
    });

    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();

        hideErrorMessages();

        const formData = {
            email: document.getElementById('email').value,
            password: document.getElementById('password').value
        };

        sendAjaxRequest('/api/users/login', 'POST', formData,
            function(data) {
                if (data.message === 'Login successful') {
                    localStorage.setItem('token', data.token);
                    window.location.href = '/dashboard';
                } else if (data.message === 'Please confirm your email') {
                    pleaseConfirm.style.display = 'block';
                } else if (data.message === 'Invalid credentials' || data.message === 'User not found') {
                    invalidCredentials.style.display = 'block';
                } else {
                    errorGeneral.style.display = 'block';
                }
            },
            function(error) {
                alert(error.responseJSON.message || 'Something went wrong, please contact us');
            }
        );
    });

    function hideErrorMessages() {
        pleaseConfirm.style.display = 'none';
        invalidCredentials.style.display = 'none';
        errorGeneral.style.display = 'none';
    }
});