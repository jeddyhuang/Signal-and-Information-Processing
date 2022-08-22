# IMPORTING THE DATA 

To load the data for lab 12, you will need to use the Python library 
pickle (https://docs.python.org/3/library/pickle.html#module-pickle) 
and Python dictionaries.

> To import pickle, simply run:

import pickle as pkl

> To retrieve the data, run:

import pickle as pkl

dictionary = pkl.load(open('lab12data/graph_sp_data.pkl', 'rb'))
A = dictionary['A']
x1 = dictionary['x1']
x2 = dictionary['x2']
x3 = dictionary['x3']
y = dictionary['y']


