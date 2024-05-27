import ("https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js")

let tit;
let body=document.getElementsByTagName("body")[0];
let dir
let inputs=document.getElementsByTagName("input");
let element;

function renombrarTitulos(){
    // body.onload=function (){
        tit=document.getElementById("tit");
    
        console.log("onlog")
        // dir=(location.href).split("/")

        dir=document.getElementsByName("hidden")[0].value
    
        // dir=dir[dir.length-1]
    
        let titulo,encabezado;
        if(dir==""){
            return null
        }
    
        if(dir=="Triangulo"){    
            encabezado="Calcular el Area de un Triangulo"
            titulo="Triangulos"
        }else if(dir=="Calificaciones"){
            encabezado="Valoracion de Calificaciones"
            titulo="Calificaciones"
    
        }else if(dir=="Grados"){
            encabezado="Conversion de Grados Farenheit a Centigrados"
            titulo="Grados"
    
        }else if(dir=="Multiplicar"){
            encabezado="Tabla de Multiplicar"
            titulo="Tabla"
    
        }else if(dir=="Viaje"){
            encabezado="Viaje Escolar"
            titulo="Viaje"
    
        }
        document.getElementsByTagName("title")[0].innerHTML=titulo
        tit.innerText=encabezado;
    // }
}

function botones_input(){
    for(let b=0;b<inputs.length;b++){
        console.log(inputs[b])
        if(inputs[b].readOnly==false){
            inputs[b].oninput=function(e){
                element=e.target;
                console.log("input")
                if(!element.validity.valid){
                    element.style.backgroundColor="red"
                }else{
                    element.style.backgroundColor=""
                }
            }
            inputs[b].ondblclick=function(e){
                element=e.target
                console.log("dblclick")
                element.value=""
                
            }
        }
    }
}

function activarEnvio() {
            
    let form=document.getElementsByTagName("form")[0]
    if(form.checkValidity()){
        form.submit();
    }
}
function AutoEnvio() {
    document.addEventListener("keydown",function(event){
        let key = event.key;
        // Verificar si la tecla presionada es la barra espaciadora
        if (key === ' ' || key === 32) {
        // Detener el evento predeterminado para evitar el desplazamiento de la página
        event.preventDefault();
        // Llamar a la función para enviar el formulario
        activarEnvio();
        }
    })
}
function EvFinDocumento(){
    renombrarTitulos();
    AutoEnvio();
    console.log("PAso el auto envio")
    botones_input();
    console.log("paso el input");
}
console.log("fin")
body.onload=function(){
    EvFinDocumento()
}