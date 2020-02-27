import numpy as np
import random
def get_order(n_samples):
    try:
        with open(str(n_samples) + '.txt') as fp:
            line = fp.readline()
            return list(map(int, line.split(',')))
    except FileNotFoundError:
        random.seed(1)
        indices = list(range(n_samples))
        random.shuffle(indices)
        return indices

def perceptron_single_step_update(
        feature_vector,
        label,
        current_theta,
        current_theta_0):
    """
    Properly updates the classification parameter, theta and theta_0, on a
    single step of the perceptron algorithm.

    Args:
        feature_vector - A numpy array describing a single data point.
        label - The correct classification of the feature vector.
        current_theta - The current theta being used by the perceptron
            algorithm before this update.
        current_theta_0 - The current theta_0 being used by the perceptron
            algorithm before this update.

    Returns: A tuple where the first element is a numpy array with the value of
    theta after the current update has completed and the second element is a
    real valued number with the value of theta_0 after the current updated has
    completed.
    """
    
    if label*(np.dot(feature_vector, current_theta)+ current_theta_0) <= 0:
        current_theta += label*feature_vector 
        current_theta_0 += label
    return (current_theta,current_theta_0)
    # Your code here

def perceptron(feature_matrix, labels, T):
    """
    Runs the full perceptron algorithm on a given set of data. Runs T
    iterations through the data set, there is no need to worry about
    stopping early.

    NOTE: Please use the previously implemented functions when applicable.
    Do not copy paste code from previous parts.

    NOTE: Iterate the data matrix by the orders returned by get_order(feature_matrix.shape[0])

    Args:
        feature_matrix -  A numpy matrix describing the given data. Each row
            represents a single data point.
        labels - A numpy array where the kth element of the array is the
            correct classification of the kth row of the feature matrix.
        T - An integer indicating how many times the perceptron algorithm
            should iterate through the feature matrix.

    Returns: A tuple where the first element is a numpy array with the value of
    theta, the linear classification parameter, after T iterations through the
    feature matrix and the second element is a real number with the value of
    theta_0, the offset classification parameter, after T iterations through
    the feature matrix.
    """
    # Your code here
    theta, theta_0 = np.zeros(len(feature_matrix[0])),0
    for t in range(T):
        
        for i in get_order(feature_matrix.shape[0]):
            theta1 = perceptron_single_step_update(feature_matrix[i],labels[i], theta,theta_0)
            theta, theta_0 = theta1[0],theta1[1]                      
            pass
    return (theta,theta_0)
    raise NotImplementedError

if __name__ == "__main__":
    print(perceptron(np.array(
        [[ 0.08082021, -0.38686205,  0.33436323,  0.3216169  ,-0.40144813],
 [-0.47458295, -0.20612913, -0.12657706, -0.46260074 ,-0.47016476],
 [ 0.21899694,  0.05526346,  0.38007593,  0.00474232 , 0.01199078],
 [-0.43513075, -0.06535535,  0.40914394,  0.11975324 ,-0.3977097 ],
 [-0.3737241 ,  0.44880352,  0.09573935, -0.24674546 , 0.27707122],
 [ 0.3299979 , -0.31142977, -0.09933898, -0.3445461  ,-0.15392703],
 [-0.0490215 , -0.46109903,  0.11003337,  0.27587126 ,-0.47248704],
 [-0.07497593,  0.34024229,  0.1712289 , -0.42741089 ,-0.48880183],
 [ 0.25227665,  0.45549924,  0.34723416, -0.2791948 , -0.48209645],
 [ 0.29643709,  0.30653357,  0.013946  ,  0.47978717,  0.12458345]]
    ),[-1,  1,  1, -1, -1,  1, -1, -1,  1,  1],5 ))
    