import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


X_train2_a = np.load("Xtrain2_a.npy")
X_train2_b = np.load("Xtrain2_b.npy")

Y_train2_a = np.load("Ytrain2_a.npy")
Y_train2_b = np.load("Ytrain2_b.npy")

X_test2_a = np.load("Xtest2_a.npy")
X_test2_b = np.load("Xtest2_b.npy")

print(X_train2_a.shape)
print(X_train2_b.shape)

print(Y_train2_a.shape)
print(Y_train2_b.shape)

print(X_test2_a.shape)
print(X_test2_b.shape)