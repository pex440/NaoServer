from distutils.log import debug
from flask import Flask,render_template,request
import qi
from NAO import NAO


app = Flask(__name__)
robotIp = "utente.local" # sto usando il robot virtuale di choregraphe
nao = NAO(robotIp)


@app.route("/",methods=["GET","POST"])        
def index():
    if request.method == "POST": 
        try:
            comando = request.json['comando']
            nao.eseguiComando(comando)
            print("Comando ricevuto",comando)
        except Exception as e:
            print(e)
        
    return render_template("index.html",comandi=nao.getMetodiUtilizzabili())

# aggiungere barra per distanza di movimento e sistemare css

        
if __name__ == "__main__":
    app.run(debug=True)