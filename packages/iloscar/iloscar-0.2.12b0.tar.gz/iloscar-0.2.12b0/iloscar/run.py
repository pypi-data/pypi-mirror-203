import os
import imp
from os.path import join

def run_test():
    file_path = imp.find_module('iloscar')[1]
    file = join(file_path,"app_test.py")
    os.system(f'python {file}')

    
