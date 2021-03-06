def operations(h, w):
    """
    Takes two inputs, h and w, and makes two Numpy arrays A and B of size
    h x w, and returns A, B, and s, the sum of A and B.

    Arg:
      h - an integer describing the height of A and B
      w - an integer describing the width of A and B
    Returns (in this order):
      A - a randomly-generated h x w Numpy array.
      B - a randomly-generated h x w Numpy array.
      s - the sum of A and B.
    """
    #Your code here
    import numpy as np
    A= np.random.rand(h,w)
    B= np.random.rand(h,w)
    return A, B, A+B
    raise NotImplementedError


A,B,s= operations(4,3)
print(A)
print()
print(B)
print()
print(s)