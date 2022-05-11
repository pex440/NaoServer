from qi import Session

class NAO:
    def __init__(self,ip,port=9559):
        self.ip = ip
        self.port= port
        self.session = Session()
        self.session.connect("tcp://"+ip+":"+str(port))
        self.motion = self.session.service("ALMotion")
    def camminaAvanti(self,quanto=0.3):
        self.motion.wakeUp()
        self.motion.moveTo(quanto,0,0)
    def camminaIndietro(self,quanto=0.3):
        self.motion.wakeUp()
        self.motion.moveTo(-quanto,0,0)
    def camminaDestra(self,quanto=0.3):
        self.motion.wakeUp()
        self.motion.moveTo(0,quanto,0)
    def camminaSinistra(self,quanto=0.3):
        self.motion.wakeUp()
        self.motion.moveTo(0,-quanto,0)
    
#NAO("192.168.1.92")