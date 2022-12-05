import matplotlib.pyplot as plt

from random_walk import RandomWalk

# while True:
rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(21, 19))
# ax.scatter(rw.x_values, rw.y_values, s=15)
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=5)
ax.plot(0, 0, linewidth=15)
ax.plot(rw.x_values[-1], rw.y_values[-1], linewidth=15)
plt.show()

    #keep_running = input("Do you want to run another plot? (y/n): ")
    #if keep_running == 'n':
        #break
