import yaml,os

def filename_constructor(loader, node):
  value = loader.construct_scalar(node)
  return '/tmp/test.log'

yaml.add_constructor(u'!filename', filename_constructor)

config = yaml.load("""
version: 1
formatters:
  simple:
    format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
handlers:
  logfile:
    class: logging.handlers.TimedRotatingFileHandler
    level: DEBUG
    filename: !filename
    backupCount: 5
    formatter: simple
""")

print config['handlers']['logfile']['filename']