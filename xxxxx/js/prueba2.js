
    var textFile = null; 
    function archivo (text) { 
        var data = new Blob([text], {type: 'text/plain'}); 
    
        // If we are replacing a previously generated file we need to 
        // manually revoke the object URL to avoid memory leaks. 
        if (textFile !== null) { 
            window.URL.revokeObjectURL(textFile); 
        } 
        
        textFile = window.URL.createObjectURL(data); 
        
        return textFile; 
    };
    
    
    let crea = document.getElementById('create'); 
    let textbox = document.getElementById('textbox'); 
    
    create.addEventListener('click', function() { 
        var link = document.getElementById('downloadlink'); 
        link.href = archivo(textbox.value); 
        link.style.display = 'block'; 
    }, false); 

