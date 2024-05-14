///Validar de Nombre
const esVacio = (palabra) => palabra.trim() === '';

const campoNombre = document.getElementById("name");

campoNombre.addEventListener("input",(evento)=>{
    validarNombre();
});

function validarNombre() {
    const nombre = campoNombre.value.trim();
    const errorNombre = document.getElementById('errorNombre');

    if (esVacio(nombre)) {
        errorNombre.style.display = 'block'; // Muestra el mensaje de error
    } else {
        errorNombre.style.display = 'none'; // Oculta el mensaje de error
    }
}

///Validar de Correo  

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


///Validar de Numero

const campoTelefono = document.getElementById("phone");

campoTelefono.addEventListener("input", () => {
    validarTelefono();
});

function validarTelefono() {
    const telefono = campoTelefono.value.trim();
    const errorPhoneInvalid = document.getElementById('errorPhoneInvalid');

    // Verifica si el número de teléfono contiene solo dígitos numéricos
    if (!/^\d*$/.test(telefono)) {
        errorPhoneInvalid.style.display = 'block'; // Muestra el mensaje de error de teléfono inválido
    } else {
        errorPhoneInvalid.style.display = 'none'; // Oculta el mensaje de error de teléfono inválido
    }
}

///Validar de Mensaje

const campoMensaje = document.getElementById("message");

campoMensaje.addEventListener("input", () => {
    validarMensaje();
});

function validarMensaje() {
    const mensaje = campoMensaje.value.trim();
    const errorMessage = document.getElementById('errorMessage');

    // Verifica si el campo de mensaje está vacío
    if (mensaje === '') {
        errorMessage.style.display = 'block'; // Muestra el mensaje de error de mensaje requerido
    } else {
        errorMessage.style.display = 'none'; // Oculta el mensaje de error de mensaje requerido
    }
}