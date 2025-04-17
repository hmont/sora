const registerForm = document.getElementById('register-form');
const registerButton = document.getElementById('register-button');

registerButton.addEventListener('click', async (e) => {
    e.preventDefault();

    const formData = new FormData(registerForm);
    const response = await fetch('/api/register', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    if (data.success) {
        alert('Registration successful');
    } else {
        alert(data.message);
    }
});