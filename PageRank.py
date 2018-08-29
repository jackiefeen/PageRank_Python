
# coding: utf-8

# # Web Science - PAGE RANK

# ### 18/03/2018
# ### EIT Digital Data Science <br> Jacqueline Neef 

# In[1]:


import numpy as np
from scipy.linalg import norm


# In[2]:


# retrieve number of pages n from the first line in the textfile
file = open("MatrixS.txt")
n = file.readline()
n = int(n)
n


# In[3]:


# read Matrix S from the text file
S = np.loadtxt("MatrixS.txt", delimiter='\t', skiprows=1, usecols=range(0,n))
S = np.mat(S)
S


# In[4]:


# damping factor
delta = 0.85

# Teleportation matrix
E = np.empty((n,n))
for x in range(n):
    for y in range(n):
        E[x,y] = 1/n
E = np.mat(E)
E


# In[5]:


# u is a row of E
u = E[0]
u = np.mat(u)
u


# In[6]:


# calculate the Google Matrix
G = delta*S+(1-delta)*E
G


# In[7]:


# Compute vector pi using the Power Method (for a fixed t)
def pi(t):
    pi = u*(G**t)
    return pi


#### Power Method: Iteration 0 ####
# calculate pi for t=0 (like by hand)
pi_0 = pi(0)
pi_0

# -> pi(0) is equal to vector u


# In[8]:


#### Power Method: Iteration 1 ####
# calculate pi for t+1 and t=0 (like by hand)
pi_1 = pi(1)
pi_1

# -> same resulting vector as in the calculation by hand


# In[9]:


#### Power Method: Iteration 2 ####
# calculate pi for t+1 and t=1 (like by hand)
pi_2 = pi(2)
pi_2

# -> same resulting vector as in the calculation by hand


# In[10]:


#### Power Method: calculation until convergence for a given epsilon ####
epsilon = 0.001
difference = 1
t=1

while (difference > epsilon):
    pi_t = pi(t)
    pi_tminus1 = pi(t-1)
    difference = norm(pi_t - pi_tminus1)
    t += 1
    print("iteration: " + str(t))
    print("current difference between pi(t) and pi(t-1):" + str(difference))

print("\n" + "**************"+ "\n" + "Converged!"+ "\n" + "Summary:" + "\n"
      + "Required number of iterations: "+ str(t)
      + "\n" + "Resulting vector pi = " + str(pi_t))

