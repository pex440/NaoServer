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

        return metodi_utilizzabili

    def eseguiComando(self,comando):
        metodi = self.getMetodiUtilizzabili()

        if comando in metodi:
            getattr(self,comando)()


    def camminaAvanti(self,quanto=0.3):
        self.motion.wakeUp()
        self.motion.moveTo(quanto,0,0)
    def camminaIndietro(self,quanto=0.3):
        self.motion.wakeUp()
        self.motion.moveTo(-quanto,0,0)
    def camminaDestra(self,quanto=0.3):
        self.motion.wakeUp()
        self.motion.moveTo(0,-quanto,0)
    def camminaSinistra(self,quanto=0.3):
        self.motion.wakeUp()
        self.motion.moveTo(0,quanto,0)

    def camminaNW(self,quanto=0.3):
        self.motion.wakeUp()
        self.motion.moveTo(quanto,quanto,0)
    def camminaNE(self,quanto=0.3):
        self.motion.wakeUp()
        self.motion.moveTo(quanto,-quanto,0)
    def camminaSW(self,quanto=0.3):
        self.motion.wakeUp()
        self.motion.moveTo(-quanto,quanto,0)
    def camminaSE(self,quanto=0.3):
        self.motion.wakeUp()
        self.motion.moveTo(-quanto,-quanto,0)
