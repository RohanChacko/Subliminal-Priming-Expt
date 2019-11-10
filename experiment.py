import sys
import os
from random import randrange

if sys.argv[1] == "0":
    categories = ['biscuits', 'choco_bis', 'juice', 'mnm', 'pool', 'skittles']
    idx = randrange(6)
    print(categories[idx])
    os.system('python expt1.py {} {}'.format(categories[idx], sys.argv[2]))
    pass
else:
    os.system('python expt2.py {}'.format(sys.argv[2]))
    pass