import matplotlib as plt
import main


fig = plt.figure()
square = fig.patch
ax1 = fig.add_axes(len(main.Square()))
square = ax1.patch
plt.show()