import sys
from weblogic_global import Profile, Data

class Newapp(Profile,Data):
    def __init__(self,appid,lifecycle):
        Profile.__init__(self,appid,lifecycle,True)
        Data.__init__(self)
        
    def display(self):
        print self.appid + '_' + self.lifecycle
        print self.user

c = Newapp(sys.argv[1],sys.argv[2])
c.display()
