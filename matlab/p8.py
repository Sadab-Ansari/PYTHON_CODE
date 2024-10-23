import matplotlib.pyplot as plt
data=[10,12,25,27,30,18]
cars=['Marcedeez','BMW','Honda City','Swift','Thar','Nano']
myexplode=[0,0,0.1,0,0,0]
mycolors=['r','g','y','b','m','c']
plt.pie(data,labels=cars,colors=mycolors)
plt.legend(title="Car Models")
plt.show()
