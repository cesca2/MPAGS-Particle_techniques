import uproot
import pandas as pd 

import numpy as np 
import matplotlib.pyplot as plt
import mplhep 

plt.style.use(mplhep.style.LHCb2)


path = './B5.root'
with uproot.open(path) as file:
    contents = file['B5']
    data_df = contents.arrays(library='pd')
    expressions = ['Dc1HitsVector_x', 'Dc1HitsVector_y', 'Dc1HitsVector_z']
    data = contents.arrays(expressions = expressions, library = 'pd')


