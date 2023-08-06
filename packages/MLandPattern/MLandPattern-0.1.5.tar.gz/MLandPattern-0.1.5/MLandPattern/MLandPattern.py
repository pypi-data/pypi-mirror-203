import numpy as np
import pandas as pd
import scipy
import math
from matplotlib import pyplot as plt


def loadCSV(pathname, class_label, attribute_names):
    """
    Extracts the attributes and class labels of an input 
    csv file dataset
    All arguments must be of equal length.
    :param pathname: path to the data file
    :param class_label: list with class label names
    :param attribute_names: list with attribute names
    :return: two numpy arrays, one with the attributes and another
            with the class labels as numbers, ranging from [0, n]
    """
    # Read the CSV file
    df = pd.read_csv(pathname, header=None)

    # Extract the attributes from the dataframe
    attribute = np.array(df.iloc[:, 0:len(attribute_names)])
    attribute = attribute.T
    
    # Re-assign the values of the class names to numeric values
    label_list = []
    for lab in df.loc[:, len(attribute_names)]:
        label_list.append(class_label.index(lab))
    label = np.array(label_list)
    return attribute, label


def vcol(vector):
    """
    Reshape a vector row vector into a column vector
    :param vector: a numpy row vector
    :return: the vector reshaped as a column vector
    """
    column_vector = vector.reshape((vector.size, 1))
    return column_vector


def vrow(vector):
    """
    Reshape a vector column vector into a row vector
    :param vector: a numpy column vector
    :return: the vector reshaped as a row vector
    """
    row_vector = vector.reshape((1, vector.size))
    return row_vector


def mean_of_matrix_rows(matrix):
    """
    Calculates the mean of the rows of a matrix
    :param matrix: a matrix of numpy arrays
    :return: a numpy column vector with the mean of each row
    """
    mu = matrix.mean(1)
    mu_col = vcol(mu)
    return mu_col


def center_data(matrix):
    """
    Normalizes the data on the dataset by subtracting the mean
    to each element.
    :param matrix: a matrix of numpy arrays
    :return: a matrix of the input elements minus the mean for
    each row
    """
    mean = mean_of_matrix_rows(matrix)
    centered_data = matrix - mean
    return centered_data


def covariance(matrix, centered = 0):
    """
    Calculates the Sample Covariance Matrix of a centered-matrix
    :param matrix: Matrix of data points
    :param centered: Flag to determine if matrix data is centered (default is False)
    :return: The data covariance matrix
    """
    if not centered:
        matrix = center_data(matrix)
    n = matrix.shape[1]
    cov = np.dot(matrix, matrix.T)
    cov = np.multiply(cov, 1/n)
    return cov


def eigen(matrix):
    """
    Calculates the eigen value and vectors for a matrix
    :param matrix: Matrix of data points
    :return: eigen values, eigen vectors
    """
    if matrix.shape[0] == matrix.shape[1]:
        s, U = np.linalg.eigh(matrix)
        return s, U
    else:
        s, U = np.linalg.eig(matrix)
        return s, U


def PCA(attribute_matrix, m):
    """
    Calculates the PCA dimension reduction of a matrix to a m-dimension sub-space
    :param attribute_matrix: matrix with the datapoints, with each row being a point
    :param m: number of dimensions of the targeted sub-space
    :return: a projection matrix P
    """
    DC = center_data(attribute_matrix)
    C = covariance(DC, 1)
    s, U = eigen(C)
    P = U[:, ::-1][:, 0:m]
    return P


def covariance_within_class(matrix_values, label):
    """
    Calculates the average covariance within all the classes in a dataset
    :param matrix_values: matrix with the values associated to the parameters of the dataset
    :param label: vector with the label values associated with the dataset
    :return: a matrix with the total average covariance within each class
    """
    class_labels = np.unique(label)
    within_cov = np.zeros((matrix_values.shape[0], matrix_values.shape[0]))
    n = matrix_values.size
    for i in class_labels:
        centered_matrix = center_data(matrix_values[:, label == i])
        cov_matrix = covariance(centered_matrix, 1)
        cov_matrix = np.multiply(cov_matrix, centered_matrix.size)
        within_cov = np.add(within_cov, cov_matrix)
    within_cov = np.divide(within_cov, n)
    return within_cov


def covariance_between_class(matrix_values, label):
    """
    Calculates the total covariance between all the classes in a dataset
    :param matrix_values: matrix with the values associated to the parameters of the dataset
    :param label: vector with the label values associated with the dataset
    :return: a matrix with the covariance between each class
    """
    class_labels = np.unique(label)
    between_cov = np.zeros((matrix_values.shape[0], matrix_values.shape[0]))
    N = matrix_values.size
    m_general = mean_of_matrix_rows(matrix_values)
    for i in range(len(class_labels)):
        values = matrix_values[:, label == i]
        nc = values.size
        m_class = mean_of_matrix_rows(values)
        norm_means = np.subtract(m_class, m_general)
        matr = np.multiply(nc, np.dot(norm_means, norm_means.T))
        between_cov = np.add(between_cov, matr)
    between_cov = np.divide(between_cov, N)
    return between_cov


def between_within_covariance (matrix_values, label):
    """
    Calculates both the average within covariance, and the between covariance of all classes on a dataset
    :param matrix_values: matrix with the values associated to the parameters of the dataset
    :param label: vector with the label values associated with the dataset
    :return:a matrix with the total average covariance within each class, and the covariance between each class
    """
    Sw = covariance_within_class(matrix_values, label)
    Sb = covariance_between_class(matrix_values, label)
    return Sw, Sb


def LDA1(matrix_values, label, m):
    """
    Calculates the Lineal Discriminant Analysis to perform dimension reduction
    :param matrix_values: matrix with the datapoints, with each row being a point
    :param label: vector with the label values associated with the dataset
    :param m: number of dimensions of the targeted sub-space
    :return: the LDA directions matrix (W), and the orthogonal sub-space of the directions (U)
    """
    class_labels = np.unique(label)
    [Sw, Sb] = between_within_covariance(matrix_values, label, class_labels)
    s, U = scipy.linalg.eigh(Sb, Sw)
    W = U[:, ::-1][:, 0:m]
    UW, _, _ = np.linalg.svd(W)
    U = UW[:, 0:m]
    return W, U


#  General method to graph a class-related data into a 2d scatter plot
def graphic_scatter_2d(matrix, labels, names, x_axis="Axis 1", y_axis="Axis 2"):
    for i in range(len(names)):
        plt.scatter(matrix[0][labels == i], matrix[1][labels == i], label=names[i])
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.legend()
    plt.show()


def logpdf_GAU_ND(x, mu, C):
    """
    Calculates the Logarithmic MultiVariate Gaussian Density for a set of vector values
    :param x: matrix of the datapoints of a dataset, with a size (n x m) 
    :param mu: row vector with the mean associated to each dimension
    :param C: Covariance matrix
    :return: a matrix with the Gaussian Density associated with each point of X, over each dimension
    """
    M = C.shape[1]
    inv_C = np.linalg.inv(C)
    [_, log_C] = np.linalg.slogdet(C)
    log_2pi = math.log(2*math.pi)
    y = np.zeros(x.shape[1]) if M == 1 else np.zeros(x.shape)
    for i in range(x.shape[1]):
        norm_x = vcol(x[:, i]) - mu
        inter_value = np.dot(norm_x.T, inv_C)
        dot_mult = np.dot(inter_value, norm_x)
        MVG = (-M*log_2pi - log_C - dot_mult)/2
        if M == 1:
            y[i] = MVG
        else:
            y[:, i] = MVG
    return y


def logLikelihood (X, mu, c):
    """
    Calculates the Logarithmic Maximum Likelihood estimator
    :param X: matrix of the datapoints of a dataset, with a size (n x m) 
    :param mu: row vector with the mean associated to each dimension
    :param c: Covariance matrix
    :return: the logarithm of the likelihood of the datapoints, and the associated gaussian density
    """
    M = c.shape[1]
    logN = logpdf_GAU_ND(X, mu, c)
    print(logN.shape)
    acum = logN.sum(1) if M != 1 else logN.sum()
    return acum