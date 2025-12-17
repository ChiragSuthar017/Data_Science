import matplotlib.pyplot as plt

print(plt.plot([1,2,3],[4,5,6]))
plt.show()

years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
Runs = [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]
plt.plot(years,Runs)
plt.xlabel("Years")
plt.ylabel("Runs Scored")
plt.title("Sachin Tandulkar's Yearly Runs")
plt.show()

# Multiple Lines in One Plot

Kohli = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]
Sehwag = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 0]

plt.plot(years, Kohli, label="Virat Kohli")
plt.plot(years, Sehwag, label="Virender Sehwag")

plt.xlabel("Year")
plt.ylabel("Runs Scored")
plt.title("Parformane Comparison")
plt.legend()
plt.show()

# Using Formate String

plt.plot(years, Kohli,'ro--', label="Virat Kohli")
plt.plot(years, Sehwag, 'g^:', label="Virender Sehwag")
plt.xlabel("Year")
plt.ylabel("Runs Scored")
plt.title("Parformane Comparison")
plt.legend()
plt.show()

# color and line Style arguments 

plt.style.use('dark_background')  # change chart style
plt.plot(years, Kohli, color='orange', linestyle='--', label="Kohli")
plt.plot(years, Sehwag, color='green', linestyle='-.', label="Sehwag")
plt.plot(years, Runs, color='blue', label="Tendulkar")
plt.xlabel("Year")
plt.ylabel("Runs Scored")
plt.title("Parformane Comparison")
plt.grid(True)
plt.legend()
plt.show()

# check style available 
print(plt.style.available)

# XKCD Comic Style
with plt.xkcd():
    plt.plot(years, Kohli, label="Kohli")
    plt.plot(years, Sehwag, label="Sehwag")
    plt.title("Epic Battle of the Batsmen")
    plt.legend()
    plt.show()

# Visualizing Tons of Data – What Crowded Looks Like
import numpy as np

for i in range(50):
    plt.plot(np.random.rand(100), linewidth=1)

plt.title("Too Much Data Can Be Confusing!")
plt.grid(True)
plt.tight_layout()
plt.show()

# matplotlib pyplot plot

# Markers
# character       description
# '.'             point marker
# ','             pixel marker
# 'o'             circle marker
# 'v'             triangle_down marker
# '^'             triangle_up marker
# '<'             triangle_left marker
# '>'             triangle_right marker
# '1'             tri_down marker
# '2'             tri_up marker
# '3'             tri_left marker
# '4'             tri_right marker
# '8'             octagon marker
# 's'             square marker
# 'p'             pentagon marker
# 'P'             plus (filled) marker
# '*'             star marker
# 'h'             hexagon1 marker
# 'H'             hexagon2 marker
# '+'             plus marker
# 'x'             x marker
# 'X'             x (filled) marker
# 'D'             diamond marker
# 'd'             thin_diamond marker
# '|'             vline marker
# '_'             hline marker

# Line Styles

# character       description
# '-'             solid line style
# '--'            dashed line style
# '-.'            dash-dot line style
# ':'             dotted line style

# Example format strings:

# 'b'    # blue markers with default shape
# 'or'   # red circles
# '-g'   # green solid line
# '--'   # dashed line with default color
# '^k:'  # black triangle_up markers connected by a dotted line
# Colors

# The supported color abbreviations are the single letter codes

# character       color
# 'b'             blue
# 'g'             green
# 'r'             red
# 'c'             cyan
# 'm'             magenta
# 'y'             yellow
# 'k'             black
# 'w'             white
# and the 'CN' colors that index into the default property cycle.