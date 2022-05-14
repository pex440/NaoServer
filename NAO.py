from qi import Session

class NAO:
    def __init__(self,ip,port=9559):
        self.ip = ip
        self.port= port
        self.session = Session()
        self.session.connect("tcp://"+ip+":"+str(port))
        self.motion = self.session.service("ALMotion")
        self.tts = self.session.service("ALTextToSpeech")
    
    def getMetodiUtilizzabili(self):
        metodi_utilizzabili = [method_name for method_name in dir(self)
                  if callable(getattr(self, method_name))]
        metodi_utilizzabili.remove("__init__")
        metodi_utilizzabili.remove("eseguiComando")
        metodi_utilizzabili.remove("getMetodiUtilizzabili")
        metodi_utilizzabili.remove("_move")
        metodi_utilizzabili.remove("getMetodiMovimento")
        metodi_utilizzabili.remove("getMetodiNonMovimento")
        return metodi_utilizzabili

    def getMetodiNonMovimento(self):
        return list(
            set(self.getMetodiUtilizzabili()) - set(self.getMetodiMovimento())
        )

    def getMetodiMovimento(self):
        metodi_movimento = self.getMetodiUtilizzabili()
        metodi_movimento.remove("say")
        return metodi_movimento
     
    # todo aggiungere metodi per varie posture 
    def eseguiComando(self,comando):
        metodi = self.getMetodiUtilizzabili()

        if comando in metodi:
            getattr(self,comando)()
    

    # tts
    def say(self,testo,lingua="italian"):
        try:
            # self.tts.setLanguage(lingua)
            self.tts.say(testo)
        except Exception as e:
            print(e)
    # fine tts


    # motion 
    def wakeUp(self):
        try:
            self.motion.wakeUp()
        except Exception as e:
            print(e)

    def _move(self,x,y,theta):
        try:
            self.motion.wakeUp()
            self.motion.moveTo(x,y,theta)
        except Exception as e:
            print(e)

    def camminaAvanti(self,quanto=0.3):
        self._move(quanto,0,0)

    def camminaIndietro(self,quanto=0.3):
        self._move(-quanto,0,0)

    def camminaDestra(self,quanto=0.3):
        self._move(0,-quanto,0)

    def camminaSinistra(self,quanto=0.3):
        self._move(0,quanto,0)

    def camminaNW(self,quanto=0.3):
        self._move(quanto,quanto,0)

    def camminaNE(self,quanto=0.3):
        self._move(quanto,-quanto,0)

    def camminaSW(self,quanto=0.3):
        self._move(-quanto,quanto,0)

    def camminaSE(self,quanto=0.3):
        self._move(-quanto,-quanto,0)
    # fine motion

if __name__ == '__main__':
    NAO("utente.local").camminaAvanti()