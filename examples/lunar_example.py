# -*- coding: utf-8 -*-
"""Example of using LUNAR for outlier detection
detection
"""
# Author: Adam Goodge <a.goodge@u.nus.edu>
#

from __future__ import division
from __future__ import print_function

import os
import sys

# temporary solution for relative imports in case pyod is not installed
# if pyod is installed, no need to use the following line
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("__file__"), '..')))

from pyod.models.lunar import LUNAR
from pyod.utils.data import generate_data
from pyod.utils.data import evaluate_print

if __name__ == "__main__":
    contamination = 0.1  # percentage of outliers
    n_train = 20000  # number of training points
    n_test = 2000  # number of testing points
    n_features = 300  # number of features

    # Generate sample data
    X_train, y_train, X_test, y_test = \
        generate_data(n_train=n_train,
                      n_test=n_test,
                      n_features=n_features,
                      contamination=contamination,
                      random_state=42)

    # train LUNAR detector
    clf_name = 'LUNAR'
    clf = LUNAR()
    clf.fit(X_train)

    y_train_scores = clf.decision_function(X_train)  # inlier scores
    y_test_scores = clf.decision_function(X_test)  # outlier scores

    # evaluate and print the results
    print("\nOn Training Data:")
    evaluate_print(clf_name, y_train, y_train_scores)
    print("\nOn Test Data:")
    evaluate_print(clf_name, y_test, y_test_scores)