const esVacio = (palabra) => {
    if (palabra.length === 0){
        return true
    }
    return false

}
const campoNombre = document.getElementById("name")
let nombre = ""

campoNombre.addEventListener("input",(evento)=>{
    nombre = evento.target.value
   
 
})

campoNombre.addEventListener("focusout",(evento)=>{
    if (esVacio(nombre)){
        document.getElementsByClassName("invalid-feedback").sty
        
    } else {
        console.log ("No es Vacio")

    }
     
})

