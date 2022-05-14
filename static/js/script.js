
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
                sendPostRequest("./",{"comando":pulsante.getAttribute("id"),"cosaDire":cosaDire}).then(()=>{
                    document.getElementById("cosaDire").value="";
                });
            }
        });
    }else{
        pulsante.addEventListener("click",()=>{
            // window.location.href = "./?comando="+pulsante.innerHTML;
            sendPostRequest('./',{"comando":pulsante.getAttribute("id")})
        })
    }
}) 
