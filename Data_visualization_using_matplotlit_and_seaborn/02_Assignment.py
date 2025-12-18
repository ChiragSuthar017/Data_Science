import matplotlib.pyplot as plt
import numpy as np

# Create a side-by-side bar chart comparing runs of Sachin, Kohli, and Sehwag over 5 selected years.

years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
Sachin = [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]
Sehwag = [0, 200, 900, 1400, 1600, 1800, 1500, 1100, 800, 0]
Kohli  = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]

x = np.arange(len(years))
width = 0.25

plt.bar(x - width, Sachin, width=width, label = "Sachin")
plt.bar(x, Sehwag, width=width, label = "Sehwag")
plt.bar(x + width, Kohli, width=width, label = "Kohli")
plt.xlabel("Years")
plt.ylabel("runs scored")
plt.title("runs comparison")
plt.xticks(x, years)
plt.legend()
plt.tight_layout()
plt.show()

# Then create a horizontal bar chart showing total runs scored in their debut 5 years.

players = ["sachin", "kohli", "sehwag"]
runs = [215+373+78+419+640, 202+689+616+847+640, 105+768+1462+1008+462]

plt.barh(players, runs , color = "skyblue")
plt.xlabel("total runs")
plt.ylabel("palyers")
plt.title("run comparison")
plt.tight_layout()
plt.show()