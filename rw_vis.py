import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Create an random walk object
rw = RandomWalk(50000)
# Set values
rw.fill_walk()
# Settings for screen
plt.figure(figsize=(10, 6.5))
# Set scatter for visualisation
plt.plot(rw.x_values, rw.y_values, linewidth = 1)
# Visualisation settings
plt.title("Random walk")
plt.xlabel("x coordinates", fontsize = 14)
plt.ylabel("y coordinates", fontsize = 14)
# Make axes unvisible
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()