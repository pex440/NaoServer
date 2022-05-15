// function that reads a json file with fetch and returns its content as a json object

function getIconAssociation(){
    return fetch('/static/js/assets/icon-associations.json')
    .then(response=>response.json())
    .then(data=>{
        return data;
    });
}


function associateIconToPulsante(pulsante){
    getIconAssociation().then(data=>{
        
        if (typeof data[pulsante.getAttribute('id')] !== "undefined"){
            pulsante.innerHTML = "";
            let icon = document.createElement("i");
            let classiDaAggiungere = data[pulsante.getAttribute("id")].split(" ");
            classiDaAggiungere.forEach(classe=>{
                icon.classList.add(classe);
            });
            pulsante.appendChild(icon);
        }    
    });
}

// console.log(readJsonFile("/static/js/assets/icon-associations.json"))

function sendPostRequest(url, data) {
    return fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
}


const pulsanti = document.querySelectorAll("button");
pulsanti.forEach((pulsante)=>{
    if (pulsante.getAttribute("id")==="say"){     // questo controllo si può migliorare, ad esempio assegnando una funzione diversa al listener
        pulsante.addEventListener("click",()=>{
            const cosaDire = document.getElementById("cosaDire").value;
            if (cosaDire!==""){
                sendPostRequest("./comandi",{"comando":pulsante.getAttribute("id"),"cosaDire":cosaDire}).then(()=>{
                    document.getElementById("cosaDire").value="";
                });
            }
        });        
    }else{
        pulsante.addEventListener("click",()=>{
            // window.location.href = "./?comando="+pulsante.innerHTML;
            sendPostRequest('./comandi',{"comando":pulsante.getAttribute("id")})
        })
    }
    associateIconToPulsante(pulsante);
}) 
