# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import csv
from itertools import zip_longest
import matplotlib.pyplot as plt
import numpy as np

size = int(input('Please enter the sample size:'))
mu_Q = int(input('Please enter mean for Q, m3/d:'))
mu_S = int(input('Please enter the mean for COD, mg/L:'))
sigma_error = float(input('Please enter the % of mean for sigma:'))

sigma_Q = sigma_error * mu_Q
sigma_S = sigma_error * mu_S

r1 = float(input('Please enter r1 for flow:'))
r2 = float(input('Please enter r1 for COD:'))

flow = []
COD = []
time = list(np.arange(0,size/2, 0.5))
flow.append(mu_Q)
COD.append(mu_S)

def function(sigma, r, size, datatype, mean):

    limit = sigma * ((3 * (1 - r**2))**0.5)
    print ('The range for random component of is from ' + str(-limit) + ' to ' + str(limit) )
    for i in range(size - 1):
        length = len(datatype)
        x1 = datatype[length - 1]
        x2 = int(mean + r * (x1 - mean) + random.uniform(-limit, limit))
        datatype.append(x2)
    return datatype

function(sigma_Q, r1, size, flow, mu_Q)
function(sigma_S, r2, size, COD, mu_S)

d = [time,flow, COD]
export_data = zip_longest(*d, fillvalue = '')

#给csv file 命名
filename = 'sigma = ' + str(sigma_error) + ', r = ' + str(r1)

with open('{}.csv'.format(filename), 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Time, hr","flowrate, m$^3$/d","substrate conc, mg/L"))
      wr.writerows(export_data)
print ('Writing completed')
myfile.close()

x = time
y1 = flow
y2 = COD
    
plt.suptitle('Time series for flowrate', fontsize = 14)
plt.ylabel('Flowrate, m$^3$/d')
plt.xlabel('time, hr')

plt.plot(x,y1)
plt.show()

plt.suptitle('Time series for COD', fontsize = 14)
plt.ylabel('Flowrate, mg/L')
plt.xlabel('time, hr')

plt.plot(x,y2)
plt.show()

