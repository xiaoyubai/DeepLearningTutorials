import cPickle
import gzip
import os
import sys
import timeit
from sklearn import linear_model, datasets
from pylab import imshow, show, cm
from sklearn.metrics import classification_report


import numpy as np


class LogisticRegression(object):

    def __init__(self, input):
        self.w = []
        self.b = []
        self.params = [self.w, self.b]
        self.input = input


    def negative_log_likelihood(self, y):
        pass

    def error(self):
        pass

def load_data(dataset):
    ''' Loads the dataset

    :type dataset: string
    :param dataset: the path to the dataset (here MNIST)
    '''

    #############
    # LOAD DATA #
    #############

    # Download the MNIST dataset if it is not present
    data_dir, data_file = os.path.split(dataset)
    if data_dir == "" and not os.path.isfile(dataset):
        # Check if dataset is in the data directory
        new_path = os.path.join(
            os.path.split(__file__)[0],
            "..",
            "data",
            dataset
        )
        if os.path.isfile(new_path) or datafile == 'mnist.pkl.gz':
            dataset = new_path

    if (not os.path.isfile(dataset)) and data_file == 'mnist.pkl.gz':
        import urllib
        origin = ('http://www.iro.umontreal.ca/~lisa/deep/data/mnist/mnist.pkl.gz')
        print 'Downloading data from %s' % origin
        urllib.urlretreve(origin, dataset)

    print '... loading data'

    # Load the dataset
    f = gzip.open(dataset, 'rb')
    train_set, valid_set, test_set = cPickle.load(f)
    f.close()
    train_set_x, train_set_y = train_set
    valid_set_x, valid_set_y = valid_set
    test_set_x, test_set_y = test_set

    return [(train_set_x, train_set_y), (valid_set_x, valid_set_y), (test_set_x, test_set_y)]

def sgd_optimization_mnist():

    # loading data in to variables
    datasets = load_data('../data/mnist.pkl.gz')
    train_set_x, train_set_y = datasets[0]
    valid_set_x, valid_set_y = datasets[1]
    test_set_x, test_set_y = datasets[2]

    ######################
    # BUILD ACTUAL MODEL #
    ######################
    print '... building the model'

    logreg = linear_model.LogisticRegression(C=1e5)

    logreg.fit(train_set_x, train_set_y)

    print logreg.get_params()

def view_image(image, label=""):
    """View a single image."""
    print ("Label: %s" % label)
    imshow(image, cmap=cm.gray)
    show()



def predict():
    pass

if __name__ == '__main__':
    sgd_optimization_mnist()
