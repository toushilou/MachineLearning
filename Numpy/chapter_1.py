__author__ = 'qyuan'

import numpy as np
import timeit

normal_py_sec = timeit.timeit('sum(x*x for x in xrange(1000))', number=10000)
naive_np_sec = timeit.timeit('sum(na*na)', setup='import numpy as np; na = np.arange(1000)',number=10000)
good_np_sec = timeit.timeit('na.dot(na)', setup='import numpy as np; na = np.arange(1000)', number=10000)

print normal_py_sec
print naive_np_sec
print good_np_sec
a = np.array([0, 1, 2, 3, 4, 5])
print a
