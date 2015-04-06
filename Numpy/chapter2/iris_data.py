__author__ = 'sweety'

from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']
print type(features)
# print data
for t, marker, c in zip(xrange(3), ">ox", "rgb"):
    print features[target == t]
    # print features[target == t, 1]
    plt.scatter(features[target == t, 0],
                features[target == t, 1],
                marker=marker,
                c=c)

plt.show()


