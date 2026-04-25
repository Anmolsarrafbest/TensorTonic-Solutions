import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # value=[]
    # for i in x:
    #     n=1+np.exp(-i)
    #     value.append(1/n)
    # return value

    x=np.asarray(x)
    n=1+np.exp(-x)
    return (1/n)