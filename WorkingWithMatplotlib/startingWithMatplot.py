import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([2020,2021,2022,2023])
ypoints = np.array([6.6,8.7,9.9,2.9])

#plt.title("India's GDP by year")
#plt.xlabel("Year")
#plt.ylabel("GDP")
#plt.grid(color = 'Yellow',linestyle = '--',linewidth=1,alpha = 0.25)
#plt.plot(xpoints,ypoints,color = 'red', alpha=1, linewidth = 9)
#plt.scatter(xpoints,ypoints,color = 'red')
#plt.bar(xpoints,ypoints,color = 'green')

#student_scores = np.array([90,91,92,93,20,34,19,99,88,24])
#plt.hist(student_scores,rwidth=0.75)
fig,ax = plt.subplots(nrows=1,ncols=2)
fig.suptitle("Multiple sub plots")
ax[0].plot(xpoints,ypoints,color='pink')

xpoints = np.array([2020,2021,2022,2023])
ypoints = np.array([-4.1,7.9,9,2.9])
ax[1].plot(xpoints,ypoints,color='green')
plt.show()