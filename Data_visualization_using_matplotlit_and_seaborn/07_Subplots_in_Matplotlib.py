import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
y1 = [i * 2 for i in x]
y2 = [i ** 2 for i in x]
y3 = [i** 0.5 for i in x]
y4 = [10 - i for i in x]

plt.subplot(1,2,1) # row, column, plot_number 
plt.plot(x, y1)
plt.title('Double of x')
plt.xlabel('Number')
plt.ylabel('Double of number')

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Square of x")
plt.xlabel('Number')
plt.ylabel('Square of number')

plt.tight_layout()
plt.show()

# 2×2 Grid of Subplots

plt.figure(figsize=(8, 6))  # make it bigger

plt.subplot(2,2,1)
plt.plot(x, y1)
plt.title('x * 2')

plt.subplot(2,2,2)
plt.plot(x, y2)
plt.title('x Square')

plt.subplot(2,2,3)
plt.plot(x, y3)
plt.title('sqrt(x)')

plt.subplot(2,2,4)
plt.plot(x, y4)
plt.title('10 - x')

plt.tight_layout()
plt.show()

# Using plt.subplots() for Clean Code

fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(x, y1)
axs[0].set_title('x*2')

axs[1].plot(x, y2)
axs[1].set_title('x**2')

fig.suptitle("My Comparison Plot", fontsize=14)
fig.subplots_adjust(top=0.85) # So title doesn't overlap
fig.savefig('my_plots.png')    # Save as image
plt.show()

# Looping Over Subplots 

fig, axs = plt.subplots(2, 2, figsize=(8, 6))
ys = [y1, y2, y3, y4]
titles = ['x * 2', 'x squared', 'sqrt(x)', '10 - x']

for i in range(2):
    for j in range(2):
        idx = i * 2 + j
        axs[i, j].plot(x, ys[idx])
        axs[i, j].set_title(titles[idx])

plt.tight_layout()
plt.show()