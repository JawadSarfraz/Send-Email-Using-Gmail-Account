class Singleton:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            return Singleton()
        return Singleton.__instance

    def __init__(self):
        #Initialize member variables
        self.emailAddr = "metest261@gmail.com"
        self.password = "Test@123"
        self.smtpUrl = "smtp.gmail.com:587"
        self.imapUrl = "imap.gmail.com"
        # check instance already created, if yes it raises the exception
        if Singleton.__instance != None:
            raise Exception("Class is singleton, eMultiple Objects are not allowed!")
        else:
            Singleton.__instance = self
