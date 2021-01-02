#In this project, we will analyze local and global temperature data 
#and compare the temperature trends where we live and favorit cities
#to overall global temperature trends.
###################################################
import pandas as pd # for dealing with data!
import matplotlib.pyplot as plt # for visualizing the data!


#importing 'global tempreature data' and cities data
globaltemp = pd.read_csv('globaldata.csv') 
citytemp1 = pd.read_csv('cairodata.csv') 
citytemp2 = pd.read_csv('athensdata.csv')
citytemp3 = pd.read_csv('madriddata.csv')

#calculating moving average
glb_mv_avg = globaltemp['avg_temp'].rolling(10).mean()
local_mv_avg1 = citytemp1['avg_temp'].rolling(10).mean()
local_mv_avg2 = citytemp2['avg_temp'].rolling(10).mean()
local_mv_avg3 = citytemp3['avg_temp'].rolling(10).mean()

#visualizing the data
plt.style.use('seaborn')
plt.plot(globaltemp['year'],glb_mv_avg,label='Global')
plt.plot(citytemp1['year'],local_mv_avg1,label='Cairo')
plt.plot(citytemp2['year'],local_mv_avg2,label='Athens')
plt.plot(citytemp3['year'],local_mv_avg3,label='Madrid')

plt.legend( loc='center right')

plt.xlabel("Years")
plt.ylabel("Temperature (°C)") 
plt.title("Cities Average Temperatures")

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.show()

