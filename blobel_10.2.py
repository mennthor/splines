import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as si


# Beispiel aus Blobel, S.231, Abb. 10.2

x = np.arange(1, 11, 1)
y = np.array([ 3.5, 2.5, 3.5, 5.5, 3.0, 2.75, 3.0, 4.0, 6.0, 6.0 ])

# Interpolate
inter_spl = si.InterpolatedUnivariateSpline(x, y)

# Fit with given spline knots t
t1 = [2, 4, 5, 8, 9]
t2 = [4, 6, 8]
fit_spl1 = si.LSQUnivariateSpline(x, y, t1)
fit_spl2 = si.LSQUnivariateSpline(x, y, t2)


xp = np.linspace(1, 10, 1000)

plt.plot(xp, inter_spl(xp), label="inter")
plt.plot(xp, fit_spl1(xp), label="fit1")
plt.plot(xp, fit_spl2(xp), label="fit2")
plt.plot(x, y, "o", label="data")
plt.xlim(0, 11)
plt.ylim(0, 8)
plt.legend(loc="best")
plt.show()