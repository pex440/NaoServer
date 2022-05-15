from qi import Session

class NAO:

    # per aggiungere un comando
    # aggiungilo ad una lista di queste e poi a metodiUtilizzabili
    # Se il nuovo comando e' accessibile dall'utente e vuoi che ci sia un'icona bootstrap
    # aggiungilo anche alla lista di icone in /static/js/assets/icon-associations.json

    metodiMovimento = [
        'camminaAvanti',
        'camminaIndietro',
        'camminaSinistra',
        'camminaDestra',
        'camminaNW',
        'camminaNE',
        'camminaSW',
        'camminaSE',
        'standUp',
        'crouch',
        'sitDown',
    ]
    
    metodiTTS = [
        'say'
    ]

    metodiNonMovimento = metodiTTS

    metodiUtilizzabili = metodiMovimento + metodiTTS

    def __init__(self,ip,port=9559):
        self.ip = ip
        self.port= port
        self.session = Session()
        self.session.connect("tcp://"+ip+":"+str(port))
        self.motion = self.session.service("ALMotion")
        self.motion.wakeUp()
        self.tts = self.session.service("ALTextToSpeech")
        self.posture = self.session.service("ALRobotPosture")
        self.dialog = self.session.service("ALDialog")
        
    # todo aggiungere metodi per varie posture 
    def eseguiComando(self,comando):
        if comando in NAO.metodiUtilizzabili:
            getattr(self,comando)()
    
    # posture
    def applyPosture(self,whichPosture,speed=0.5):
        try:
            self.posture.applyPosture(whichPosture,speed)
        except Exception as e:
            print(e)

    def crouch(self):
        self.applyPosture("Crouch")

    def sitDown(self):
        self.applyPosture("Sit")
    def standUp(self):
        self.applyPosture("Stand")
    # fine posture

    # tts
    def say(self,testo,lingua="italian"):
        #self.dialog.setLanguage(lingua)
        try:
            # self.tts.setLanguage(lingua)
            self.tts.say(testo)
        except Exception as e:
            print(e)
    # fine tts


    # motion 
    def _wakeUp(self):
        try:
            self.motion.wakeUp()
        except Exception as e:
            print(e)

    def _move(self,x,y,theta):
        try:
            self._wakeUp()
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
    NAO("192.168.1.16").eseguiComando("camminaAvanti")
