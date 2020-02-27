def hinge_loss_single(feature_vector, label, theta, theta_0):
    """
    Finds the hinge loss on a single data point given specific classification
    parameters.

    Args:
        feature_vector - A numpy array describing the given data point.
        label - A real valued number, the correct classification of the data
            point.
        theta - A numpy array describing the linear classifier.
        theta_0 - A real valued number representing the offset parameter.


    Returns: A real number representing the hinge loss associated with the
    given data point and parameters.
    """
    import numpy as np
    feature_vector,theta = np.array(feature_vector), np.array(theta)
    return max([0, 1 -label*(np.dot(feature_vector, theta)+theta_0) ])
    # Your code here
    raise NotImplementedError


if __name__ == "__main__":
    print(hinge_loss_single([1,2,3], -1, [3,2,1], 5))    