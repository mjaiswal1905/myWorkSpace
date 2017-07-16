import sys
import weblogic_global

def display():
    print wls.appid
    print wls.lifecycle

if __name__ == '__main__':
    wls = weblogic_global.Profile(sys.argv[1],sys.argv[2])
    display()
