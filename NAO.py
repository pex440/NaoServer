from qi import Session

class NAO:
    def __init__(self,ip,port=9559):
        self.ip = ip
        self.port= port
        self.session = Session()
        self.session.connect("tcp://"+ip+":"+str(port))
        self.motion = self.session.service("ALMotion")
    
    def getMetodiUtilizzabili(self):
        metodi_utilizzabili = [method_name for method_name in dir(self)
                  if callable(getattr(self, method_name))]
        metodi_utilizzabili.remove("__init__")
        metodi_utilizzabili.remove("eseguiComando")
        metodi_utilizzabili.remove("getMetodiUtilizzabili")
        metodi_utilizzabili.remove("move")

        return metodi_utilizzabili
    # todo aggiungere metodi per varie posture e metodo say
    def eseguiComando(self,comando):
        metodi = self.getMetodiUtilizzabili()

        if comando in metodi:
            getattr(self,comando)()

    def wakeUp(self):
        try:
            self.motion.wakeUp()
        except Exception as e:
            print(e)

    def move(self,x,y,theta):
        try:
            self.motion.wakeUp()
            self.motion.moveTo(x,y,theta)
        except Exception as e:
            print(e)

    def camminaAvanti(self,quanto=0.3):
        self.move(quanto,0,0)

    def camminaIndietro(self,quanto=0.3):
        self.move(-quanto,0,0)

    def camminaDestra(self,quanto=0.3):
        self.move(0,-quanto,0)

    def camminaSinistra(self,quanto=0.3):
        self.move(0,quanto,0)

    def camminaNW(self,quanto=0.3):
        self.move(quanto,quanto,0)

    def camminaNE(self,quanto=0.3):
        self.move(quanto,-quanto,0)

    def camminaSW(self,quanto=0.3):
        self.move(-quanto,quanto,0)

    def camminaSE(self,quanto=0.3):
        self.move(-quanto,-quanto,0)

if __name__ == '__main__':
    NAO("utente.local").camminaAvanti()