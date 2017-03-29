import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

my_data = pd.read_csv('DJA.csv', index_col='Date')
#print(my_data)
my_data.index = pd.to_datetime(my_data.index)
years, changes = [],[]
for i in range(1886,2016):
    year = str(i)
    change = my_data[year].ix[-1]['DJIA'] / my_data[year].ix[0]['DJIA']
    years.append(year)
    changes.append(change)
    
yearly_change = pd.DataFrame(changes)
yearly_change.index = years
print (yearly_change)
#print yearly change
sample_mean = np.mean(yearly_change)
print ('sample_mean :', sample_mean[0])
#print sample mean
sample_standard = np.std(yearly_change)
print ('sample_standard :' ,sample_standard[0])
#print sample standard
standard_1, standard_2, standard_3 =[], [], []
for n in yearly_change.index:
    if abs(yearly_change[0][n] - sample_mean)[0] > sample_standard[0]:
        standard_1.append(n)
    if abs(yearly_change[0][n] - sample_mean)[0] > (2 * sample_standard[0]):
        standard_2.append(n)
    if abs(yearly_change[0][n] - sample_mean)[0]> (3 * sample_standard[0]):
        standard_3.append(n)
print ('1 standard deviation from the mean:',standard_1 )
print ('2 standard deviation from the mean:',standard_2 )
print ('3 standard deviation from the mean:',standard_3 )
#plot the normal probablity plot of the sequence of yearly change for Dow index
x=np.arange(yearly_change.min(),yearly_change.max(),0.1)
plt.plot(x,stats.norm.cdf(x,loc=sample_mean, scale=sample_standard),marker='*')