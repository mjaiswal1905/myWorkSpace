import os
import logging

class ClassProfile:
    def __init__(self,appid,lifecycle,verbose=False):
        self.APPID, self.LIFECYCLE = appid, lifecycle
        self.TXAPPID = self.APPID+'_'+self.LIFECYCLE

        self.logger = logging.getLogger('PROFILE')
        if verbose:
            self.logger.info('APPID=%s'%self.APPID)
            self.logger.info('LIFECYCLE=%s'%self.LIFECYCLE)

class ClassData:
    def __init__(self,verbose=False):
        self.USER='wladmin'
        self.logger = logging.getLogger('DATA')
        if verbose:
            self.logger.info('USER=%s'%self.USER)

class ClassPath:
    def __init__(self):
        self.script_path=os.path.join(os.sep,os.path.dirname(os.path.realpath(__file__)),'script.py')
        self.logger = logging.getLogger('PROFILE')