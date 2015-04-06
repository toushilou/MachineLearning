__author__ = 'sweety'

from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']
print type(data)
print dir(data)
target_names = data.target_names
print features

labels = target_names[target]
for t, marker, c in zip(xrange(3), ">ox", "rgb"):
    # print features[target == t, 1]
    plt.scatter(features[target == t, 0],
                features[target == t, 1],
                marker=marker,
                c=c)

plength = features[:, 2]
print type(plength)
is_setosa =  (labels == 'setosa')
print is_setosa
plt.show()


