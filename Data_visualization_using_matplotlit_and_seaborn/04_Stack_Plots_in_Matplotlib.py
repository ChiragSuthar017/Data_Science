import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]
studying = [3,4,3,5,4,3,4]
playing = [2,2,1,1,2,3,2]
watching_tv = [2,1,2,2,1,1,1]
sleeping = [5,5,6,5,6,5,5]

label = ['studying', 'playing', 'watching_tv', 'sleeping']
color = ['blue', 'skyblue', 'pink', 'red']

plt.figure(figsize=(6,6))
plt.stackplot(days, studying,playing , watching_tv, sleeping, labels=label, colors=color, alpha=0.8)
plt.legend(loc='upper left')
plt.title("weekly activity tracker")
plt.xlabel('days')
plt.ylabel('hours')
plt.grid(True)
plt.show()