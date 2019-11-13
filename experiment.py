from random import randrange
import sys
import os
import expt1
import expt2


fixation_delay = sys.argv[2]

log = open('log.txt', 'w')

name = input('Name of participant: ')
sex = input('Gender (M/F): ').upper()

# Experiment 1 => Color based
# Experiment 2 => Brand based
# Run this file as python experiment.py <<expt_no->[1/2]>> <<fixation_delay>>

if sys.argv[1] == "1":

    # clock = init()
    keypress, primed_with, appeared_first, order = expt1.main(fixation_delay)


elif sys.argv[1] == "2":

    categories = ['biscuits', 'choco_bis', 'juice', 'mnm', 'pool', 'skittles']
    idx = randrange(6)
    print(categories[idx])

    keypress, primed_with, appeared_first, order = expt2.main(categories[idx], fixation_delay)

else :
    pass
