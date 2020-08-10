console.log("Vinculado");

//https://www.youtube.com/watch?v=M4LaQ3KUGOM&t=242s
//https://www.w3schools.com/js/js_ajax_xmlfile.asp
//https://makeitrealcamp.gitbook.io/javascript-book/manipulacion-de-archivos
//https://www.youtube.com/watch?v=k0-cP3nMiqw

/*importacion de modulo "fs", proporciona una API para interacuar
con el sistema de archivos de manera similar a las funciones estandar POSIX*/
//const fs = require('fs');

document.querySelector('#regCategoria').addEventListener('click', traerDatos);

/*function creacionJsonCategorias(){
    /**Crea el archivo JSON en caso de que este no exista 
    nuevaCat = document.getElementById("nuevaCat").nodeValue;
    miObjeto = {categoria:[]};
    miObjeto.categoria = new Array();
    miObjeto.categoria.push(nuevaCat);
    miJSON = JSON.stringify(miObjeto);
    
    fs.appendFile("../archivosJson/categorias.json", miJSON, (err)=>{
        if(err){
            throw err;
        }
        console.log("El archivo ha sido creado exitosamente")
    });
}*/

function traerDatos(){
    /**Trae los datos desde el archivo JSON especificado */
    console.log("Extrallendo datos")
    const xhttp = new XMLHttpRequest();
    xhttp.open('GET', '../site/archivosJson/categorias.json', true);
    xhttp.send()
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            let datos = JSON.parse(this.responseText);
            console.log(datos);
            console.log("*********************");
            agregarCategoria(datos);
        }
    }
}

function agregarCategoria(objeto){
    nuevaCat = document.getElementById("nuevaCat").nodeValue;
    objeto.categorias.push("nuevo");
    console.log(objeto);
    myJSON = JSON.stringify(objeto);
}

/*function verificaExistenciaArchivo(){
    Comprueba la existencia de archivo JSON categorias
    fs.stat("documento.json", function(err){
        if(err == null){
            console.log("El archivo existe");
            traerDatos();
        }
        else if(err.code == 'ENOENT'){
            //************** Creando el archivo 
            console.log("El archivo no existe");
            creacionJsonCategorias();
        }
        else{
            console.log(err)//ocurrio algun error
        }
    });
}*/