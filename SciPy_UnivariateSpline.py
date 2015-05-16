import numpy as np
import scipy.interpolate as si
import matplotlib.pyplot as plt

# Known function values = N equally spaced data points
N = 10
x = np.linspace(0, 10, N)
y = np.sin(x)**2

# Find the interpolating cubic spline. It goes through all data points (x,y)
tck = si.splrep(x, y)

# Construct a smoothing cubic spline with less points than data points given
smooth = si.UnivariateSpline(x, y, s=0.1)


# Plot values for the underlying true function (x2,yt)
x2 = np.linspace(0, 10, 200)
yt = np.sin(x2)**2

# Plot values for resulting spline (x2,y2)
y2 = si.splev(x2, tck)

# Plot values for smoothing spline (x2, y3)
y3 = smooth(x2)

# Plot used knots, splines and true function
plt.plot(x, y, 'o', label="knots")
plt.plot(x2, yt, label="true")
plt.plot(x2, y2, label="spline")
plt.plot(x2, y3, label="smooth")
plt.legend(loc="best")
plt.show()