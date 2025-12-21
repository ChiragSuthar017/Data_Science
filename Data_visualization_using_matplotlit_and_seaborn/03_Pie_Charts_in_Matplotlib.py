import matplotlib.pyplot as plt

plt.style.use("ggplot")

# basic pie charts
label = ["Sachin", "Sehwag", "Kohli", "Yuvraj"]
runs = [18000, 8000, 12000, 9500]

plt.title("Career Runs Of Indian Batsman")
plt.pie(runs, labels=label)
plt.show()

# Custom Colors
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
plt.pie(runs, labels=label, colors=colors)
plt.show()

# Add Edges and Style Slices with wedgeprops
plt.pie(
    runs,
    labels=label,
    colors=colors,
    wedgeprops={'edgecolor': 'black', 'linewidth': '1', 'linestyle': '--'}
)
plt.show()

# Highlight a Slice Using explode

expload = [0.1,0,0,0]
plt.pie(runs, labels=label, explode=expload, colors=colors)
plt.title("Expload pie chart example")
plt.show()

# Add Shadows for a 3D Feel
plt.pie(
    runs,
    labels=label,
    colors=colors,
    explode=expload,
    shadow=True
)
plt.show()

# Start Angle
# Use startangle to rotate the pie for better alignment.

plt.pie(
    runs,
    labels=label,
    explode=expload,
    colors=colors,
    shadow=True,
    startangle=140
)
plt.show() 

# Show Percentages with autopct

plt.pie(
    runs,
    labels=label,
    autopct='%1.1f%%'
)
plt.title("Career Runs Share")
plt.show()

# Crowded Pie Chart – Why to Avoid

# Too many categories
languages = ['Python', 'Java', 'C++', 'JavaScript', 'C#', 'Ruby', 'Go', 'Rust', 'Swift', 'PHP']
usage = [30, 20, 10, 10, 7, 5, 4, 3, 2, 1]

plt.pie(usage, labels=languages, autopct='%1.1f%%', startangle=90)
plt.title("Programming Language Usage (Crowded Example)")
plt.show()

# Why avoid it?

# Hard to compare slice sizes visually
# Cluttered and confusing
# No clear insight
# Better alternatives: bar charts or horizontal bar chart