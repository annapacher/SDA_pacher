# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:09:58 2019

@author: Anna
"""

import numpy as np
import matplotlib



# First step: generate bivariate normal distribution with mean 0 and covariance
# matrix being the identity

# Box muller: generate random variables for absolute value of a (exponentially distributed with lamdba = 1)
# and angle phi (uniformly distributed in the intervall [0, 2pi] (in polar coordinates)
a = np.random.exponential(1,size=1000)
phi = np.random.uniform(low=0,high=2*np.pi,size=1000)

# transform to cartesian coordinates
x = a*np.cos(phi)
y = a*np.sin(phi)
# plot as gree plus
matplotlib.pyplot.plot(x,y,'r+')


#Second step: generate bivariate normal distribution with mean 0 and
#covariance matrix A (see below)

#generate different Covariance Matrix A
A = [[3, 1],[1, 1]]

#extract eigenvalues and eigenvectors
A_eig = np.linalg.eig(A)

#now construct Jordan Decomposition of A (A=GLG')
E_val = A_eig[0]   #get eigenvalues
Gamma = A_eig[1]   #get eigenvectors
Lambda=np.diag(E_val)
AA = np.dot(np.dot(Gamma,Lambda) , np.transpose(Gamma))
#should be similar to A

#Checks
AA=A #might be false in some component
np.allclose(AA, A) #should be True

Lambda12=np.sqrt(Lambda)
A12 = np.dot(np.dot(Gamma,Lambda12) , np.transpose(Gamma))

#inverse of A can now be calculated by inverse of Lambda
#Goal: create 2 dim point cloud with this


c=[x,y]
cA = np.dot(A12,c)
matplotlib.pyplot.plot(cA[0],cA[1],'g+')
