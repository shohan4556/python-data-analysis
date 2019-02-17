import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
#print(data.iloc[0:,])

# find out all the number's operator
# mail id contain nummeric value (prefix or postfix)

phone = data.iloc[:,1]
gp = 0
robi = 0
airtel = 0
banglalik = 0
teletalk = 0

for n in phone:
    value = str(n)

    if value[1] == '7' or value[1] == '3':
        gp += 1
        #print('gp')
    elif value[1] == '8':
        robi += 1
    elif value[1] == '6':
        airtel += 1
    elif value[1] == '5':
        teletalk += 1
    elif value[1] == '9':
        banglalik += 1

    # some number stars from 88 exclude them
    # print(value[1])

datalist = [gp, robi, banglalik, teletalk, airtel]
print(datalist)

#print("Total GP Numbers "+str(gp))
#print("Total Robi Numbers "+str(robi))
#print("Total Banglalink Numbers "+str(banglalik))
#print("Total Teletalk Numbers "+str(teletalk))
#print("Total Airtel Numbers "+str(airtel))

dbin = 0

for i in range(20):
    dbin += 5
    #print(dbin)

#plt.hist(datalist, dbin, edgecolor='white', linewidth = 1)
#plt.plot(datalist)
plt.scatter(datalist, [100,80,60,40,20])

plt.xlabel('Use Sim Operator')
plt.ylabel('Number of User')
plt.grid(True)

testY = [100,80,60,40,20]
text = ['gp','robi','banglalink','teletalk','airtel']

for x, valX in enumerate(datalist):
    for y, valY in enumerate(testY):
        plt.text(datalist[x], testY[x], text[x])
        #plt.text(val, y, text[x])

plt.show()

