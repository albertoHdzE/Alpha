#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#argument[1] number of nodes
#argument[2] d1
#argument[3] d2


#import pip
#import subprocess
#import numpy as np
#import os
#os.popen("sudo -S %s"%('su'), 'w').write('1')

#import sys
#sys.path.insert(0, '/Users/beto/WolframWorkspaces/Base/Alpha/pyphi')

#os.system("python /Users/beto/WolframWorkspaces/Base/Alpha/pyphi/setup.py")

#sys.path.insert(0,  '/Users/beto/anaconda/pkgs/conda-4.2.9-py35_0/lib/python3.5/site-packages/conda/common')

#subprocess.Popen(['python','setup.py'], cwd='/Users/beto/WolframWorkspaces/Base/Alpha/pyphi/')
#pip.main(['install','requirements.txt'], cwd='/Users/beto/WolframWorkspaces/Base/Alpha/pyphi/')

#python_env_var = {"_", "__PYVENV_LAUNCHER__"}
#CMD_ENVIRONMENT = {name: value for (name, value) in os.environ.items() 
#                   if name not in python_env_var}  
#subprocess.call('./pip install -r /Users/beto/WolframWorkspaces/Base/Alpha/pyphi/requirements.txt', shell=True, 
#                env=CMD_ENVIRONMENT)

#subprocess.call('./pip install -r /Users/beto/WolframWorkspaces/Base/Alpha/pyphi/requirements.txt', shell=True) 


#import pyphi


#=================================
#d1 = np.array([0.66667,0,0,0.33333])
#d2 = np.array([0.5,0,0,0.5])
#n=2
# This assumes the distributions are over `n` nodes
#d1 = d1.reshape([2] * 2)
#d2 = d2.reshape([2] * 2)

#dd=pyphi.utils.hamming_emd(d1, d2)
#print(dd)
#=================================

import numpy as np
import pyphi
import sys

d1 = np.array(eval(sys.argv[2]))
d2 = np.array(eval(sys.argv[3]))
n=int(sys.argv[1])

# This assumes the distributions are over `n` nodes
#d1 = d1.reshape([int(sys.argv[1])] * int(sys.argv[1]))
#d2 = d2.reshape([int(sys.argv[1])] * int(sys.argv[1]))

d1 = d1.reshape([2] * n)
d2 = d2.reshape([2] * n)

#old version
#dd=pyphi.utils.hamming_emd(d1, d2)
#new version
dd=pyphi.distance.hamming_emd(d1, d2)
print(dd)
#dd.stdout