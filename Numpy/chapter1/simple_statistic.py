__author__ = 'sweety'

import scipy as sp

data = sp.genfromtxt("../data/web_traffic.tsv", delimiter='\t')
print data[:10]
print data.shape
