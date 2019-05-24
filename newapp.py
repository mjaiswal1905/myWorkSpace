import sys
import os
import yaml
import logging.config
import weblogic_global as wls

class ClassNewapp(wls.ClassProfile,wls.ClassData,wls.ClassPath):
    def __init__(self,appid,lifecycle):
        wls.ClassProfile.__init__(self,appid,lifecycle,True)
        wls.ClassData.__init__(self,True)
        wls.ClassPath.__init__(self)
        self.log_file = os.path.join(os.sep,os.path.dirname(os.path.realpath(__file__)),'newapp.log')
        self.yaml_config = os.path.join(os.sep,os.path.dirname(os.path.realpath(__file__)),'logging.yaml')
        self.log_level = 'INFO'
        
    def constructor_logfilename(self, loader, node):
        value = loader.construct_scalar(node)
        return self.log_file

    def constructor_loglevel(self, loader, node):
        value = loader.construct_scalar(node)
        return self.log_level

    def configure_logging(self):
        yaml.SafeLoader.add_constructor(u'!logfilename', self.constructor_logfilename)
        yaml.SafeLoader.add_constructor(u'!loglevel', self.constructor_loglevel)
        try:
            logging.config.dictConfig(yaml.safe_load(open(self.yaml_config, 'r')))
        except ValueError as e:
            print e
            sys.exit(1)
        self.logger = logging.getLogger('NEWAPP')

    def show(self):
        #print self.APPID + '_' + self.LIFECYCLE
        #print self.USER
        self.logger.info('APPID=%s'%self.APPID)

if __name__ == '__main__':
    ObjectNewapp = ClassNewapp(sys.argv[1],sys.argv[2])
    ObjectNewapp.configure_logging()
    ObjectNewapp.show()