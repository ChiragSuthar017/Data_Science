import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set_theme(style='darkgrid') # set themes

x = np.array([0,2,3,4,5,6,7,8,9,10,60])
y = np.sin(x)

sns.lineplot(x=x , y=y)
plt.title('Beautiful line plot')
plt.show()