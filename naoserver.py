from distutils.log import debug
from flask import Flask,render_template,request
import qi
from NAO import NAO


app = Flask(__name__)
# robotIp = "utente.local" # sto usando il robot virtuale di choregraphe
# nao = NAO(robotIp)

nao = None

def confermaRicezione(comando,args=[]):
    if args:
        print("Comando ricevuto",comando,"con argomenti",args)
    elif not args:
        print("Comando ricevuto",comando)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/comandi",methods=["GET","POST"])        
def comandi():
    global nao
    if request.method == "GET":
        if request.args:
            if request.args.get("robotIp") and not request.args.get("robotPort"):
                nao = NAO(request.args.get("robotIp"))
            elif request.args.get("robotPort") and request.args.get("robotIp"):
                nao = NAO(request.args.get("robotIp"),request.args.get("robotPort"))
    print(nao.ip, nao.port)

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
    return render_template("comandi.html",robotIp=nao.ip,robotPort=nao.port,comandiNonMovimento=NAO.metodiNonMovimento,comandiMovimento=NAO.metodiMovimento)

# aggiungere barra per distanza di movimento e sistemare css

        
if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0",port=5000)