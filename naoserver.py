from distutils.log import debug
from flask import Flask,render_template,request
import qi
from NAO import NAO


app = Flask(__name__)
robotIp = "utente.local" # sto usando il robot virtuale di choregraphe
nao = NAO(robotIp)

def confermaRicezione(comando,args=[]):
    if args:
        print("Comando ricevuto",comando,"con argomenti",args)
    elif not args:
        print("Comando ricevuto",comando)



@app.route("/",methods=["GET","POST"])        
def index():
    if request.method == "POST": 
        try:
            comando = request.json['comando']
            if comando=="say":
                cosaDire = request.json['cosaDire']
                nao.say(cosaDire)
                confermaRicezione(comando,args=[cosaDire])
            else:
                nao.eseguiComando(comando)
                confermaRicezione(comando)
        except Exception as e:
            print("Exception: ",e)
        
    return render_template("index.html",comandiNonMovimento=nao.getMetodiNonMovimento(),comandiMovimento=nao.getMetodiMovimento())

# aggiungere barra per distanza di movimento e sistemare css

        
if __name__ == "__main__":
    app.run(debug=True)