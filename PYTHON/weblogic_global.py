class Profile:
    def __init__(self,appid,lifecycle,verbose=False):
        self.appid = appid
        self.lifecycle = lifecycle
        if verbose:
            print self.appid
            print self.lifecycle

class Data:
    def __init__(self):
        self.user='wladmin'