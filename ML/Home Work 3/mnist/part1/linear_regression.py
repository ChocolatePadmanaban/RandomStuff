import numpy as np

### Functions for you to fill in ###

def closed_form(X, Y, lambda_factor):
    """
    Computes the closed form solution of linear regression with L2 regularization

    Args:
        X - (n, d + 1) NumPy array (n datapoints each with d features plus the bias feature in the first dimension)
        Y - (n, ) NumPy array containing the labels (a number from 0-9) for each
            data point
        lambda_factor - the regularization constant (scalar)
    Returns:
        theta - (d + 1, ) NumPy array containing the weights of linear regression. Note that theta[0]
        represents the y-axis intercept of the model and therefore X[0] = 1
    """
    
    # theta = np.linalg.lstsq(X, Y, rcond= lambda_factor)
    # return theta[0]
    sparce_matrix= np.linalg.inv(np.dot(X.T,X)+lambda_factor*np.identity(X.shape[1]))
    return np.dot(sparce_matrix, np.dot(X.T,Y))



### Functions which are already complete, for you to use ###

def compute_test_error_linear(test_x, Y, theta):
    test_y_predict = np.round(np.dot(test_x, theta))
    test_y_predict[test_y_predict < 0] = 0
    test_y_predict[test_y_predict > 9] = 9
    return 1 - np.mean(test_y_predict == Y)

if __name__ == "__main__":
    print(closed_form(np.array([[0.88856403, 0.07364357],
 [0.49178183, 0.17217236],
 [0.23117118, 0.11301024],
 [0.10512479, 0.49187898],
 [0.95320948, 0.48723216],
 [0.80128333 ,0.31639344],
 [0.55954956, 0.26649954],
 [0.15778914 ,0.20477695],
 [0.82053581, 0.82500487],
 [0.35403556 ,0.48881738],
 [0.00210498, 0.29977032],
 [0.50019624 ,0.0901699 ],
 [0.51176633, 0.43434358],
 [0.74870499 ,0.10461389]]), np.array([0.58156596 ,0.2654023,  0.61359839, 0.22780854 ,0.43781348, 0.23820277,
 0.86599915, 0.1464218,  0.80283055 ,0.92706583, 0.75555283, 0.11510406,
 0.49722314, 0.56494575]), 0.1374976783571441))


