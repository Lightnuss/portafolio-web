//Validacion de login (Email)
const campoEmail = document.getElementById("email");

campoEmail.addEventListener("input", () => {
    validarEmail();
});

function validarEmail() {
    const email = campoEmail.value.trim();
    const errorEmailRequired = document.getElementById('errorEmailRequired');
    const errorEmailInvalid = document.getElementById('errorEmailInvalid');

    // Verifica si el campo de correo electrónico está vacío
    if (email === '') {
        errorEmailRequired.style.display = 'block'; // Muestra el mensaje de error de correo electrónico requerido
        errorEmailInvalid.style.display = 'none'; // Oculta el mensaje de error de correo electrónico inválido
    } else {
        errorEmailRequired.style.display = 'none'; // Oculta el mensaje de error de correo electrónico requerido

        // Verifica si el formato del correo electrónico es válido
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            errorEmailInvalid.style.display = 'block'; // Muestra el mensaje de error de correo electrónico inválido
        } else {
            errorEmailInvalid.style.display = 'none'; // Oculta el mensaje de error de correo electrónico inválido
        }
    }
}

//Validacion de login (Contraseña)
const campoContraseña = document.getElementById("password");

campoContraseña.addEventListener("input", () => {
    validarContraseña();
});

function validarContraseña() {
    const contraseña = campoContraseña.value.trim();
    const errorPassword = document.getElementById('errorPassword');

    // Verifica si la contraseña está vacía
    if (contraseña === '') {
        errorPassword.style.display = 'block'; // Muestra el mensaje de error de contraseña requerida
    } else {
        errorPassword.style.display = 'none'; // Oculta el mensaje de error de contraseña requerida
    }
}