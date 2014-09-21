# Assignment 1, Part 3: Nearest Neighbor Classification

import math
import random
from assignment_one_kmeans import read_data, \
    num_unique_labels, euclidean_squared


def get_fold_indices(n, V, fold):

    pass


def nn_classifier(point, train_data, train_labels, k, K):

    pass


def classification_error(classifier, data, labels):

    pass


def main():

    data_file = 'seeds_dataset_shuffled.txt'
    instances, labels = read_data(data_file)

    # want labels run from 0 through K-1
    # not 1 through K
    labels = [i-1 for i in labels]

    print 'Read %d instances and %d labels from file %s.' \
        % (len(instances), len(labels), data_file)

    if len(instances) != len(labels):
        raise Exception('Expected equal number of instances and labels.')
    else:
        n = len(instances)

    # Find number of clusters by finding out how many unique elements are there
    # in labels.
    K = num_unique_labels(labels)
    print 'Found %d unique labels.' % K

    # k-nearest neighbor classification for various k
    k_range = range(1, 31)

    # create empty list to store cross-validation errors for different k
    cv_error = []

    for k in k_range:

        total_error = 0.0

        # 5 fold cross-validation
        for fold in range(5):
            fold_train_indices, fold_test_indices = \
                get_fold_indices(n, 5, fold)
            train_data = []
            train_labels = []
            classifier = lambda point: 0

            test_data = []
            test_label = []
            fold_error = classification_error(classifier,
                                              test_data, test_label)

            total_error += fold_error

        cv_error.append(total_error/5)

    for i in range(len(k_range)):
        print k_range[i], cv_error[i]


if __name__ == '__main__':
    main()
