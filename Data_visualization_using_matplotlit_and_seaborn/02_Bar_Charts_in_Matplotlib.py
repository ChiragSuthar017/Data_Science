import matplotlib.pyplot as plt
import numpy as np

years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
runs = [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]

# basic bar plot

plt.bar(years, runs)
plt.xlabel("years")
plt.ylabel("runs scorrd")
plt.title("Sachin Tandulkar's Yearly Runs")
plt.show()

# Setting Bar Width & Side-by-Side Bar Charts

Sachin = [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]
Sehwag = [0, 200, 900, 1400, 1600, 1800, 1500, 1100, 800, 0]
Kohli  = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]

x = np.arange(len(years))
width = 0.25

plt.bar(x - width, Sachin, width=width, label = "Sachin")
plt.bar(x, Sehwag, width=width, label = "Sehwag")
plt.bar(x + width, Kohli, width=width, label = "Kohli")
plt.xlabel("Years")
plt.ylabel("Runs Scored")
plt.title("Run Comparison")
plt.xticks(x, years) # Show actual year instead of 0,1,2,...
plt.legend()
plt.tight_layout()
plt.show()

# Horizontal Bar Charts with barh()

players = ["Sachin", "Sehwag", "Kohli", "Yuvraj"]
runs_5yrs = [500+700+1100+1500+1800, 0+200+900+1400+1600, 0+0+500+800+1100, 300+600+800+1100+900]

plt.barh(players, runs_5yrs, color="skyblue")
plt.xlabel("Total Runs in First 5 Years")
plt.ylabel("First 5-Year Performance of Indian Batsmen")
plt.tight_layout()
plt.show()

# Adding Value Labels with plt.text()\

players = ["sachin", "sehwag", "kohli"]
runs = [1500, 1200, 1800]

plt.bar(players, runs, color = "red")

# Add label on top of bar
for i in range(len(players)):
    plt.text(i, runs[i] + 30, str(runs[i]), ha = 'center')

plt.ylabel("Runs")
plt.title("Runs Scored by Players")
plt.tight_layout()
plt.show()
