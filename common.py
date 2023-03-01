import os
import sys

def input_path(file):
    try:
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), file)
    except:
        return os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), file)