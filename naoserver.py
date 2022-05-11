from flask import Flask,render_template,request
import qi
from NAO import NAO
app = Flask(__name__)

robotIp = "utente.local" # sto usando il robot virtuale di choregraphe

@app.route("/")
def index():
    if request.method == "GET": # todo: passare alle richieste POST
        comando = request.values.get('comando')
        if comando is not None:
            if comando == "camminaAvanti":
                nao = NAO(robotIp)
                nao.camminaAvanti()
            elif comando == "camminaIndietro":
                nao = NAO(robotIp)
                nao.camminaIndietro()
            
               

    return render_template("index.html",comandi=[
        "camminaAvanti",
        "camminaIndietro"
    ])

if __name__ == "__main__":
    app.run(debug=True)