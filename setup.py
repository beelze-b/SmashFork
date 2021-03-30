import glob
import os
import setuptools

# with open("README.txt", "r") as fh:
#     long_description = fh.read()

setuptools.setup(name = 'smash',
	             version = open("smash/_version.py").readlines()[-1].split()[-1].strip("\"'"),
	             description = 'SMaSH: A scalable, general marker gene identification framework for single-cell RNA sequencing and Spatial Transcriptomics',
	             author = 'Simone Riva',
	             author_email = 'sgr34@cam.ac.uk',
	             url = 'https://gitlab.com/cvejic-group/smash',
	             license='LICENSE',
	             classifiers = ['Programming Language :: Python :: 3.5'],
	             python_requires='>=3.5',
	             packages=setuptools.find_packages(where='smash'),
	             package_dir={'': 'smash'},
	             py_modules=[os.path.splitext(os.path.basename(path))[0] for path in glob.glob('smash/*.py')],
# 	             install_requires=['NumPy>=1.18',
# 	                               'Pandas>=0.25',
# 	                               'matplotlib>=3.1',
# 	                               'scikit-learn>=0.21',
# 	                               'seaborn>=0.9',
# 	                               'Tensorflow>=1.12']
	             )
