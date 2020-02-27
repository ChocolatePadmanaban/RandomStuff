def hinge_loss_full(feature_matrix, labels, theta, theta_0):
    """
    Finds the total hinge loss on a set of data given specific classification
    parameters.

    Args:
        feature_matrix - A numpy matrix describing the given data. Each row
            represents a single data point.
        labels - A numpy array where the kth element of the array is the
            correct classification of the kth row of the feature matrix.
        theta - A numpy array describing the linear classifier.
        theta_0 - A real valued number representing the offset parameter.


    Returns: A real number representing the hinge loss associated with the
    given dataset and parameters. This number should be the average hinge
    loss across all of the points in the feature matrix.
    """
    # Your code here
    import numpy as np
    feature_matrix,theta, labels = np.array(feature_matrix), np.array(theta), np.array(labels)
    loss_vector= [ max([0, 1 -labels[i]*(np.dot(feature_matrix[i], theta)+theta_0) ]) for i  in range(len(feature_matrix))]
    return sum(loss_vector)/len(loss_vector)
    raise NotImplementedError

if __name__ == "__main__":
    print(hinge_loss_full([[1,2,3],[4,5,6]], [-1,1], [3,2,1], 5)) 