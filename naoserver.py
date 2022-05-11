from distutils.log import debug
from flask import Flask,render_template,request
import qi
from NAO import NAO


app = Flask(__name__)
robotIp = "utente.local" # sto usando il robot virtuale di choregraphe
nao = NAO(robotIp)
@app.route("/")
def index():
    if request.method == "GET": # todo: passare alle richieste POST
        comando = request.values.get('comando')
        nao.eseguiComando(comando)
        
        return render_template("index.html",comandi=nao.getMetodiUtilizzabili())

        
if __name__ == "__main__":
    app.run(debug=True)