import argparse
import getopt
import os
import sys
from .server import Serve


def myF(argv):
    arg_port = 2000
    help_file = open
    arg_help = open(os.path.dirname(__file__) + "\help.txt", "r").read()
    
    try:
        opts, args = getopt.getopt(argv[1:], "hi:p:", ["help", "port"])
    except getopt.GetoptError:
        print(arg_help)
        sys.exit(0)
    else:
        if len(opts) > 0:
            for opt, arg in opts:
                if opt in ("-h", "--help"):
                    print(arg_help)
                    sys.exit(0)
                elif opt in ("-p", "--port"):
                    arg_port = arg
                    #print("User")
                else:
                    print(arg_help)
                    sys.exit(0)
    Serve(arg_port)
    
if __name__ == "__main__":
    myF(sys.argv)