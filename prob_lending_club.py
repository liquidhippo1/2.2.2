import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import numpy as np

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True) # no idea what this line means


#loansData = loansData.splitlines() # we could also do data.split('\n')
#loansData = [i.split(', ') for i in loansData]

# Now, convert create a pandas dataframe
#column_names = loansData[0] # this is the first row
#data_rows = loansData[1::] # these are all the following rows of data
#df = pd.DataFrame(data_rows, columns=column_names)

loansData.boxplot(column='Amount.Requested')
plt.show()

loansData.hist(column='Amount.Requested')
plt.show()



plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()