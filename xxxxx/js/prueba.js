
/************** importacion de modulo "fs", proporciona una API para interacuar
con el sistema de archivos de manera similar a las funciones estandar POSIX*/
const fs = require('fs');

//************** funcion de creacion de archivo */
function creacionJsonCategorias(){    
    fs.appendFile("../archivosJson/documento.json", myJson, (err)=>{
        if(err){
            throw err;
        }
        console.log("El archivo ha sido creado exitosamente")
    });
}


/*nombreCat = document.getElementById("nuevaCat").value;
var myObject = new Object();
myObject.categoria = new Array();
myObject.categoria.push(nombreCat);

var myJson = JSON.stringify(myObject);*/



//************** */
//var myObject = {names:["Braulio", "Israel", "Garcia", "Martinez"], edad:20, ciudad:"Tonala"};
//var myObject = {categorias:[]}
//myObject.categoria = new Array();
//myObject.categorias.push('Verduras');

//var myJson = JSON.stringify(myObject);//convierte un objeto JS a untexto de notacion JSON
var myObject = JSON.parse()

//************** Verificacion de existencia de un archivo */
fs.stat("documento.json", function(err){
    if(err == null){
        console.log("El archivo existe");
    }
    else if(err.code == 'ENOENT'){
        //************** Creando el archivo */
        creacionJsonCategorias();
    }
    else{
        console.log(err)//ocurrio algun error
    }
});