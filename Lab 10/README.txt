# IMPORTING THE DATA 

To load the data for lab 10, you will need to use the Python library 
pickle (https://docs.python.org/3/library/pickle.html#module-pickle) 
and Python dictionaries.

> To import pickle, simply run:

import pickle as pkl

> To retrieve the dataset (faces) and the dataset average (mu) and 
covariance (sigma), run:

dictionary = pkl.load(open('lab10data.pkl','rb'))
faces = dictionary['faces']  # shape = (112,92,40)
mu = dictionary['mu']        # shape = (112,92)
sigma = dictionary['sigma']  # shape = (10304,10304)

# DATASET DESCRIPTION

A link for the dataset in its original format can be found here: 
http://www.seas.upenn.edu/~ese224/labs/att_faces.zip 

The ORL face database
---------------------

This directory contains a set of faces taken between April 1992 and
April 1994 at the Olivetti Research Laboratory in Cambridge, UK.

There are 10 different images of 40 distinct subjects. For some of the
subjects, the images were taken at different times, varying lighting
slightly, facial expressions (open/closed eyes, smiling/non-smiling)
and facial details (glasses/no-glasses).  All the images are taken
against a dark homogeneous background and the subjects are in
up-right, frontal position (with tolerance for some side movement).

The files are in PGM format and can be conveniently viewed using the 'xv'
program. The size of each image is 92x112, 8-bit grey levels. The images
are organised in 40 directories (one for each subject) named as:

		sX

where X indicates the subject number (between 1 and 40). In each directory
there are 10 different images of the selected subject named as:

		Y.pgm

where Y indicates which image for the specific subject (between 1 and 10).

When using these images, please give credit to Olivetti Research Laboratory.
A convenient reference is the face recognition work which uses some of
these images:

 F. Samaria and A. Harter 
  "Parameterisation of a stochastic model for human face identification"
  2nd IEEE Workshop on Applications of Computer Vision
  December 1994, Sarasota (Florida).

The paper is available via anonymous ftp from quince.cam-orl.co.uk and is
stored in pub/users/fs/IEEE_workshop.ps.Z

If you have any question, please email Ferdinando Samaria: fs@cam-orl.co.uk

