import yaml,os,sys

APPID = sys.argv[1]

def filename_constructor(loader, node):
  value = loader.construct_scalar(node)
  return '/tmp/' + APPID + '.log'

yaml.SafeLoader.add_constructor(u'!filename', filename_constructor)

file   = 'C:\workSpace\logging.yaml'
config = yaml.safe_load(open(file,'r').read())

print config['handlers']['file_handler']['filename']